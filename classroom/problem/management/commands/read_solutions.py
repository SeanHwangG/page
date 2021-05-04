import logging
import traceback
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from problem.models import Problem, Site, Solution, Tag, User
from gitbook.models import Repository


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-u', '--user_email', required=True, type=str, help="user_email")
    parser.add_argument('-t', '--tag_glob', type=str, help="Glob path for each tag")
    parser.add_argument('-tt', '--tag_type', type=str, help="Set group for tags")

  def parse_problems(self, repo: Repository, user: User, tag: Tag, tag_path: Path):
    logging.info("parse_problems(%s, %s, %s)", user, tag, tag_path)

    new_solution = 0
    for problem_path in tag_path.glob("*"):
      if "_" not in problem_path.name[:-3]:
        continue
      site_code, problem_code = problem_path.name[:-3].split("_", 1)
      site = Site.objects.get(code=site_code)
      problem, created = Problem.objects.get_or_create(site=site, code=problem_code)
      problem.tags.set([tag])
      url_path = str(problem_path.resolve()).split('interview/', 1)[1]
      solution, created = Solution.objects.update_or_create(user=user, problem=problem, defaults={
          "link": f"{repo.url}/tree/main/{url_path}"})
      if created:
        new_solution += 1
        logging.info("Created : solution %s", solution)

    return new_solution

  def handle(self, tag_glob: str, user_email: str, tag_type: str, *args, **options):
    logging.info("handle(%s, %s, %s)", tag_glob, user_email, tag_type)
    new_tag, new_solution = 0, 0
    user = User.objects.get(email=user_email)
    repo = Repository.objects.get(user=user)
    try:
      for tag_path in Path(repo.path_env).glob(tag_glob):
        logging.debug(tag_path)
        tag_type, tag_name = str(tag_path).rsplit("/", 2)[1:]
        tag, created = Tag.objects.get_or_create(name=tag_name, type=tag_type)
        if created:
          new_tag += 1
          logging.info("Created : tag %s", tag)
        new_solution += self.parse_problems(user, tag, tag_path)
      logging.info("Created : %s tags from directory", new_tag)
      logging.info("Created : %s solutions from directory", new_solution)
    except ObjectDoesNotExist:
      logging.exception("Not found")
