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
    parser.add_argument('-d', '--embed_dir', type=str, help="base glob path (default note embed_dir)")
    parser.add_argument('-g', '--glob', type=str, help="glob path (base/glob)")
    parser.add_argument('-p', '--problem', help="Whether to add problem meta info", action="store_true")
    parser.add_argument('-l', '--lang_tag', help="Whether to add language tag (ex: ```py ..code.. ```)", action="store_true")

  def handle(self, *args, **options):
    logging.info(f"{options}")
    if options["problem"]:
      embed_dirs = Path(".").glob(options["dir"])
      for embed_dir in embed_dirs:
        if not embed_dir.is_dir():
          continue
        out = pathlib.Path(f"{embed_dir}.md").open('w')
        logging.info(f"Writing output to {embed_dir}.md")
        paths = embed_dir.glob(options["glob"])
        path_problems = [(path, Problem.objects.get_or_create(problem_id=path.stem, site_id=path.stem[:2])[0]) for path in paths]
        path_problems = list(sorted(path_problems, key=lambda path_problem: (path_problem[1].site_id, path_problem[1].level)))
        for i, (path, problem) in enumerate(path_problems):
          if problem.site_id == "LC":
            level = ["", "Easy", "Medium", "Hard"][int(problem.level)]
          elif problem.site_id == "BJ":
            level = int(problem.level)
          else:
            level = problem.level
          if i == 0 or path_problems[i - 1][1].site_id != problem.site_id:
            out.write(f"\n\n> {problem.site_id}")
          out.write(f"\n\n * [lv {level} : {problem.title}]({problem.link}) [(edit)]({settings.PROBLEM_GITHUB}/edit/main/{str(path).split('interview/', 1)[1]})\n\n")
          out.write(path.read_text())
        logging.info(f"Total embeded problems : {len(path_problems)}")
    else:
      for embed_dir in Path(".").glob(options["embed_dir"]):
        out = pathlib.Path(f"{embed_dir}.md").open('w')
        for f in Path(".").glob(options["glob"]):
          out.write(f.read_text())
