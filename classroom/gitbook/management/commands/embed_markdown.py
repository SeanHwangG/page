import argparse
import fileinput
import logging
import pathlib
import re

from django.core.management.base import BaseCommand, CommandError

logging.basicConfig(level=logging.DEBUG)

EMBED_RE = r"{% include \'(.*)\' %}"


class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('-p', '--path', type=str, help="glob path for markdown", default="*.md")
    parser.add_argument('-b', '--back', action="store_true", help="glob path for markdown")

  def reset_backup(glob_markdown):
    logging.info(glob_markdown)
    cur_path = pathlib.Path(".")

    n_reset = 0
    for file_path in pathlib.Path(".").glob(f"{glob_markdown}.bak"):
      file_path.rename(file_path.with_suffix(''))
      n_reset += 1
    logging.info(
        f"Reset : {n_reset} documents")

  def embed_markdowns(glob_markdown):
    logging.info(glob_markdown)
    cur_path = pathlib.Path(".")

    for file_path in pathlib.Path(".").glob(glob_markdown):
      logging.info(file_path)
      if "SUMMARY" in file_path.stem:
        continue
      embeds = []
      with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
          m = re.match(EMBED_RE, line)
          if m:
            embeds.append(m.group(1))
            p = file_path.parent / m.group(1)
            print(p.read_text())
          else:
            print(line, end="")
      logging.info(
          f"Embeded : {len(embeds)} markdowns")
      for n in embeds:
        logging.debug(
            f"File : {n}")

  if __name__ == "__main__":
    args = get_parser()
    if args["back"]:
      reset_backup(args["path"])
    else:
      embed_markdowns(
          args["path"])
