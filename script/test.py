import subprocess
import argparse
import logging
from .common import run_command


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--all", action="store_true")
  parser.add_argument("--lint", action="store_true")
  parser.add_argument("--django", action="store_true")
  return parser.parse_args()


if __name__ == "__main__":
  args = get_args()
  returncode = 0
  if args.all or args.lint:
    returncode |= run_command("pycodestyle --statistics --exclude env,migrations,settings.py,.git --indent-size=2 --config .pylintrc .")
  if args.all or args.django:
    returncode |= run_command("python manage.py test")
  logging.info(f"Returncode : {returncode}")
  exit(returncode)
