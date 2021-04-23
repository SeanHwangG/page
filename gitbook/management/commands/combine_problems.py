from django.core.management.base import BaseCommand, CommandError
from gitbook.models import Gitbook, Header
from django.conf import settings
from problem.models import Problem
import io
import logging
import yaml
import panflute
from pathlib import Path


class Command(BaseCommand):
  help = 'Closes the specified poll for voting'

  def add_arguments(self, parser):
    parser.add_argument('-d', '--dir', type=str, help="dir path or glob dir path (it will be result filename of markdown)")
    parser.add_argument('-f', '--file', type=str, required=True, help="Glob path relative to dir")
    parser.add_argument('-r', '--result_dir', type=str, help="Directory to put result markdown")

  def handle(self, dir="", file="", result_dir="", **options):
    logging.info(f"handle({dir}, {file}, {result_dir}, {lang_tag}, {problem})")
    dirs = list(Path(".").glob(dir))
    logging.info(f"{dirs}")

    for dir in dirs:
      if not dir.is_dir():
        continue
      out = Path(f"{result_dir}/{dir.name}.md").open('w')
      paths = dir.glob(file)
      site = Site.objects.get(name=path.stem[:2])
      path_problems = [(path, Problem.objects.get_or_create(name=path.stem, site=site)[0]) for path in paths]
      path_problems = list(sorted(path_problems, key=lambda path_problem: (path_problem[1].name, path_problem[1].level)))
      for i, (path, problem) in enumerate(path_problems):
        if problem.site_id == "LC":
          level = ["", "Easy", "Medium", "Hard"][int(problem.level)]
        elif problem.site_id == "BJ":
          level = int(problem.level)
        else:
          level = problem.level
        if i == 0 or path_problems[i - 1][1].site_id != problem.site_id:
          out.write(f"\n\n> {problem.site.name}")
        url_path = str(path.resolve()).split('interview/', 1)[1]
        out.write(f"\n\n * [lv {level} : {problem.title}]({problem.link}) [(edit)]({settings.PROBLEM_GITHUB}/edit/main/{url_path})\n\n")
        out.write(path.read_text())
      logging.info(f"Wrote : {out.name}")
      logging.info(f"Processed : {len(path_problems)} problems")
    logging.info(f"Processed : {len(dirs)} markdowns")
