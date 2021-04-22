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
    parser.add_argument('-f', '--file', type=str, required=True, help="Path or glob path relative to dir path (base/glob)")
    parser.add_argument('-r', '--result_dir', type=str, help="Directory to put result markdown")
    parser.add_argument('-l', '--lang_tag', help="Whether to add language tag (ex: ```py ..code.. ```)", action="store_true")
    parser.add_argument('-p', '--problem', help="Whether to add problem meta info", action="store_true")

  def handle(self, dir="", file="", result_dir="", lang_tag=False, problem=False, **options):
    logging.info(f"handle({dir}, {file}, {result_dir}, {lang_tag}, {problem})")
    if problem:
      dirs = list(Path(".").glob(dir))
      logging.info(f"{dirs}")

      for dir in dirs:
        if not dir.is_dir():
          continue
        out = Path(f"{result_dir}/{dir.name}.md").open('w')
        paths = dir.glob(file)
        site = Site.objects.get(name=path.stem[:2])
        path_problems = [(path, Problem.objects.get_or_create(name=path.stem, site=site)[0]) for path in paths]
        path_problems = list(sorted(path_problems, key=lambda path_problem: (path_problem[1].site_id, path_problem[1].level)))
        for i, (path, problem) in enumerate(path_problems):
          if problem.site_id == "LC":
            level = ["", "Easy", "Medium", "Hard"][int(problem.level)]
          elif problem.site_id == "BJ":
            level = int(problem.level)
          else:
            level = problem.level
          if i == 0 or path_problems[i - 1][1].site_id != problem.site_id:
            out.write(f"\n\n> {problem.site.name}")
          out.write(f"\n\n * [lv {level} : {problem.title}]({problem.link}) [(edit)]({settings.PROBLEM_GITHUB}/edit/main/{str(path.resolve()).split('interview/', 1)[1]})\n\n")
          out.write(path.read_text())
        logging.info(f"Wrote : {out.name}")
        logging.info(f"Processed : {len(path_problems)} problems")
      logging.info(f"Processed : {len(dirs)} markdowns")
    else:
      for dir in Path(".").glob(dir):
        out = pathlib.Path(f"{result_dir}/{dir}.md").open('w')
        for f in Path(".").glob(file):
          out.write(f.read_text())
