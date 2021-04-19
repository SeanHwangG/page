import io
import logging
from pathlib import Path
import re
import traceback
import panflute
import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from problem.models import Solution, Problem, Site, Tag
from user.models import Membership, User
from util.crawler import crawl_solutions


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_id', type=str, help="Type of problem site_id", choices=["BJ", "LC"])
    parser.add_argument('-p', '--problem_dir', type=str, help="Glob path for local solutions")
    parser.add_argument('-t', '--team_id', type=str, help="team_id")
    parser.add_argument('-u', '--user_id', type=str, help="user_id")
    parser.add_argument('-nt', '--n_thread', action="store_true", help="Number of thread to parse solutions (default all available)", default=None)

  def handle(self, *args, problem_dir=None, site_id=None, team_id=None, user_id=None, n_thread=None, **options):
    logging.info(f"handle({problem_dir}, {site_id}, {team_id}, {user_id}, {n_thread})")
    assert problem_dir or site_id, "Wrong Params : site_id must be set for team_id or user_id"
    assert sum([bool(team_id), bool(user_id), bool(problem_dir)]) == 1, "Wrong params : One of problem, team_id, user_id should be set"

    try:
      if problem_dir:
        site_ids = set(site.site_id for site in Site.objects.all())
        new_tag = new_solution = 0
        for file in Path(".").glob(problem_dir):
          logging.debug(file)
          tag_id, title = str(file).rsplit("/", 2)[1:]
          tag, created = Tag.objects.get_or_create(tag_id=tag_id)
          if title[:2] not in site_ids:
            pass
          if created:
            new_tag += 1
            logging.info(f"Created : tag {tag}")

          site_id, problem_id = title[:-3].split("_", 1)
          try:
            problem = Problem.objects.get(problem_id=f"{site_id}_{problem_id}", site_id=site_id)
          except Exception as e:
            logging.warn(traceback.format_exc())
            continue
          problem.tags.set(Tag.objects.filter(tag_id=tag_id))
          solution, created = Solution.objects.update_or_create(user=User.objects.get(user_id="rbtmd1010"), problem=problem, defaults={
                                                                "link": f"{settings.PROBLEM_GITHUB}/tree/main/{str(file.resolve()).split('interview/', 1)[1]}"})
          if created:
            new_solution += 1
            logging.info(f"Created : solution {solution}")
        logging.info(f"Created : {new_tag} tags from directory")
        logging.info(f"Created : {new_solution} solutions from directory")
      else:
        if team_id:
          users = User.objects.filter(membership__team_id=team_id)
        elif user_id:
          users = User.objects.filter(user_id=user_id)
        for solution_dic in crawl_solutions(users.values_list(f"{site_id}_id", flat=True), site_id, n_thread):
          unseen_total, seen_total = 0, 0
          for problem_id in solution_dic["problem_ids"]:
            _, unseen_created = Problem.objects.get_or_create(problem_id=problem_id, site_id=site_id)
            _, seen_created = Solution.objects.update_or_create(user=User.objects.get(user_id=solution_dic["user_id"]), problem_id=problem_id)
            unseen_total, seen_total = unseen_total + int(unseen_created), seen_total + int(seen_total)
          logging.info(f"Created : {unseen_total} new problems, {seen_total} solutions by {solution_dic['user_id']} solved")
    except Exception as e:
      logging.error(traceback.format_exc())
