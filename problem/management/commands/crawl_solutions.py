import io
import logging
import pathlib
import re
import panflute
import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from markdown.models import Header, Markdown
from problem.models import Solution, Problem, Site, Tag
from user.models import Membership, User
from util.crawler import crawl_solutions


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-p', '--problem', type=str, help="Glob path for local solutions")
    parser.add_argument('-s', '--site_id', type=str, help="Type of problem site_id", choices=["BJ", "LC"], required=True)
    parser.add_argument('-t', '--team_id', type=str, help="team_id")
    parser.add_argument('-u', '--user_id', type=str, help="user_id")
    parser.add_argument('-nt', '--n_thread', action="store_true", help="Number of thread to parse solutions (default all available)", default=None)

  def handle(self, *args, **options):
    logging.info(f"handle({options})")
    assert len({"team_id", "user_id", "problem"} & set(options.keys())) != 1, "One of problem, team_id, user_id should be set"
    site_ids = set(site.site_id for site in Site.objects.all())

    try:
      if options["problem"]:
        for file in settings.NOTE_DIR.glob(options["problem"]):
          tag_id, title = str(file).rsplit("/", 2)[1:]
          tag, _ = Tag.objects.update_or_create(tag_id=tag_id, group="algorithm")
          if title[:2] not in site_ids:
            pass

          relative_path = str(file.relative_to(settings.NOTE_DIR))
          site_id, problem_id = title[:-3].split("_", 1)
          problem = Problem.objects.get(problem_id=f"{site_id}_{problem_id}")
          problem.tags.set(Tag.objects.filter(tag_id=tag_id))
          solution, _ = Solution.objects.update_or_create(user=User.objects.get(user_id="rbtmd1010"), problem=problem, defaults={"link": f"{settings.NOTE_GITHUB}/{relative_path}"})
      else:
        if options["team_id"]:
          users = User.objects.filter(membership__team_id=options["team_id"])
        elif options["user_id"]:
          users = User.objects.filter(user_id=options["user_id"])
        for solution_dic in crawl_solutions(users.values_list(f"{options['site_id']}_id", flat=True), options["site_id"], options["n_thread"]):
          for problem_id in solution_dic["problem_ids"]:
            problem = Problem.objects.get(problem_id=problem_id)
            Solution.objects.update_or_create(user=User.objects.get(user_id=solution_dic["user_id"]), problem=problem)
    except Exception as e:
      logging.error(e)
