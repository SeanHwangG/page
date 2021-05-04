import argparse
import logging
import pathlib

from django.conf import settings
from django.core.management import call_command

from .common import run_command


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--clean", action="store_true")
  parser.add_argument("-p", "--crawl_problems", action="store_true")
  return parser.parse_args()


def get_backup():
  logging.info("get_backup")
  for json_backup in sorted(settings.BASE_DIR.glob("data/*.json")):
    call_command("loaddata", str(json_backup))
  return 0


if __name__ == "__main__":
  args = get_args()
  if args.clean:
    run_command("rm -rf db.sqlite3")

  if run_command("python manage.py migrate") or get_backup():
    exit(1)

  if args.crawl_problems:
    call_command("crawl_problems", site_code="BJ")
