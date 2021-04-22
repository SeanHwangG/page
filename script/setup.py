import argparse
import logging
import os
from operator import itemgetter
from django.contrib.auth.models import User
from .common import run_command


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--sqlite", action="store_true")
  return parser.parse_args()


def create_db():
  logging.info("create_db()")
  DB_NAME, DB_USER, DB_PASSWORD = itemgetter("DB_NAME", "DB_USER", "DB_PASSWORD")(os.environ)
  os.environ["PGPASSWORD"] = DB_PASSWORD
  returncode = run_command(f'psql -c "CREATE USER {DB_USER}"')
  returncode |= run_command(f'psql -c "CREATE DATABASE {DB_NAME} WITH OWNER {DB_USER}"')
  return returncode


def setup_db():
  logging.info("setup_db()")
  return run_command("python manage.py migrate")


def create_superuser():
  logging.info("create_superuser()")
  admin_ids = os.environ.get("DJANGO_ADMIN_IDS").split(",")
  admin_pws = os.environ.get("DJANGO_ADMIN_PASSWORDS").split(",")
  admin_emails = os.environ.get("DJANGO_ADMIN_EMAILS").split(",")

  for admin_id, admin_pw, admin_email in zip(admin_ids, admin_pws, admin_emails):
    if not User.objects.filter(username=admin_id).exists():
      User.objects.create_superuser(admin_id, admin_email, admin_pw)
  return 0


if __name__ == "__main__":
  args = get_args()
  if not args.sqlite and create_db():
    exit(1)
  if setup_db() or create_superuser():
    exit(1)
