import os
import logging
import traceback
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from classroom.problem.models import Problem, Site, Solution, Tag, User
from classroom.gitbook.models import Repository


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-u', '--user_email', required=True, type=str, help="user_email")

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

  def handle(self, user_email: str, *args, **options):
    logging.info("handle(%s)", user_email)
    new_tag, new_solution = 0, 0
    user = User.objects.get(email=user_email)
    repo = Repository.objects.get(user=user)
    assert repo.path_env in os.environ, f"{repo.path_env} not in invironment"
    local_path = os.getenv(repo.path_env)
    try:
      for tag_type_path in Path(local_path).glob(repo.tag_type_glob):
        logging.debug(tag_type_path)
        for tag_path in Path(tag_type_path).glob(repo.tag_glob):
          logging.debug(tag_path)
          tag, created = Tag.objects.get_or_create(name=tag_path.name, type=tag_type_path.name)
          if created:
            new_tag += 1
            logging.info("Created : tag %s", tag)
          new_solution += self.parse_problems(repo, user, tag, tag_path)
        logging.info("Created : %s tags from directory", new_tag)
        logging.info("Created : %s solutions from directory", new_solution)
    except ObjectDoesNotExist:
      logging.exception("Not found")
