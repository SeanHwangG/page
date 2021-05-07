import io
import logging
import os
from pathlib import Path

import panflute
import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from classroom.gitbook.models import Repository
from classroom.problem.models import Problem, Site
from classroom.user.models import User


class Command(BaseCommand):
  help = 'Combine solutions with problem information for gitbook'

  def add_arguments(self, parser):
    parser.add_argument('-u', '--user_email', type=str, required=True, help="user email")
    parser.add_argument('-r', '--result_dir', type=str, required=True, help="Directory to put result markdown")

  def combine_problems(self, site: Site, tag_path: Path, repo: Repository):
    logging.debug("combine_problems(%s , %s, %s)", site, tag_path, repo)
    path_problems = [(path, Problem.objects.get_or_create(code=path.stem[3:], site=site)[0])
                     for path in tag_path.glob(f"{site.code}_*")]
    path_problems.sort(key=lambda path_problem: (path_problem[1].level, path_problem[1].code,))
    lines = []
    for i, (path, problem) in enumerate(path_problems):
      url = str(path.resolve()).split('interview/', 1)[1]
      raw_level, title, link = problem.raw_level, problem.title, problem.link
      lines += [f"\n\n * [Level {raw_level} : {title}]({link}) [(edit)]({repo.url}/edit/main/{url})\n\n"]
      lines += [path.read_text()]
    logging.debug("Processed : %s problems", len(path_problems))
    return lines

  def handle(self, user_email: str, result_dir: str, *args, **options):
    logging.info("handle(%s, %s)", user_email, result_dir)
    user = User.objects.get(email=user_email)
    repo = Repository.objects.get(user=user)
    assert repo.path_env in os.environ, f"path_env is not set : {repo.path_env}"
    local_repo = Path(os.getenv(repo.path_env))

    logging.info("Combining solution from %s", local_repo)
    for tag_type_path in local_repo.glob(repo.tag_type_glob):
      for tag_path in tag_type_path.glob(repo.tag_glob):
        logging.debug("From tag_path %s", local_repo)
        if not tag_path.is_dir():
          continue
        out = (local_repo / result_dir / f"{tag_path.name}.md").open('w')
        for site in Site.objects.filter():
          logging.debug("From site %s", site)
          lines = self.combine_problems(site, tag_path, repo)
          if len(lines):
            out.write(f"\n\n> {site.name}")
          for i, line in enumerate(lines):
            out.write(line)
