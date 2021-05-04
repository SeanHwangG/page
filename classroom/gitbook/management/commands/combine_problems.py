import io
import logging
import os
from pathlib import Path

import panflute
import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from gitbook.models import Repository
from problem.models import Problem, Site
from user.models import User


class Command(BaseCommand):
  help = 'Closes the specified poll for voting'

  def add_arguments(self, parser):
    parser.add_argument('-u', '--user_email', type=str, help="user email")
    parser.add_argument('-t', '--tag_glob', type=str, help="glob tag path (result filename of markdown)")
    parser.add_argument('-tt', '--tag_type_glob', type=str, help="glob tag type path")
    parser.add_argument('-r', '--result_dir', type=str, help="Directory to put result markdown")

  def combine_problems(self, site: Site, tag_path: Path, repo: Repository):
    logging.debug("combine_problems(%s , %s, %s)", site, tag_path, repo)
    path_problems = [(path, Problem.objects.get_or_create(code=path.stem[3:], site=site)[0])
                     for path in tag_path.glob(f"{site.code}_*")]
    path_problems.sort(key=lambda path_problem: (path_problem[1].level, path_problem[1].code,))
    lines = []
    for i, (path, problem) in enumerate(path_problems):
      if site.code == "LC":
        level = ["", "Easy", "Medium", "Hard"][int(problem.level)]
      elif site.code == "BJ":
        level = int(problem.level)
      else:
        level = problem.level
      url = str(path.resolve()).split('interview/', 1)[1]
      lines += [f"\n\n * [Level {level} : {problem.title}]({problem.link}) [(edit)]({repo.url}/edit/main/{url})\n\n"]
      lines += [path.read_text()]
    logging.debug("Processed : %s problems", len(path_problems))
    return lines

  def handle(self, user_email: str, tag_type_glob: str, tag_glob: str, result_dir: str, *args, **options):
    logging.info("handle(%s, %s, %s)", user_email, tag_glob, result_dir)
    user = User.objects.get(email=user_email)
    repo = Repository.objects.get(user=user)
    try:
      local_repo = Path(os.getenv(repo.path_env))
    except TypeError:
      logging.exception("path_env is not set : %s", repo.path_env)
      exit(1)

    logging.info("Combining solution from %s", local_repo)
    for tag_type_path in local_repo.glob(tag_type_glob):
      for tag_path in tag_type_path.glob(tag_glob):
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
