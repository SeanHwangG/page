from problem.models import Tag, Problem, Site
from util.crawler import crawl_problems
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from operator import itemgetter
import io
import logging
import yaml
import pathlib
import panflute
import re


class Command(BaseCommand):
  help = 'Update problem level'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_code', type=str, help="glob path for problems", choices=["BJ", "CC", "CF", "LC", "KT", "HR"])
    parser.add_argument('-nt', '--n_thread', type=int, help="Whether to parse problems in multithreading (default all available)", default=None)

  def handle(self, *args, site_code=None, n_thread=None, **options):
    logging.info(f"handle({site_code}, {n_thread})")
    site = Site.objects.get(code=site_code)
    total = 0

    # Only crawl problems within our database
    if site_code == "HR":
      problem_ids = list(Problem.objects.filter(code="HR").values_list('problem_id', flat=True))
    elif site_code == "CC":
      problem_ids = list(Problem.objects.filter(code="CC").values_list('problem_id', flat=True))
    else:
      problem_ids = None

    for problem_dic in crawl_problems(site_code, n_thread, problem_ids):
      link, problem_code, level, title = itemgetter("link", "problem_code", "level", "title")(problem_dic)
      _, created = Problem.objects.update_or_create(site=site, code=problem_code, defaults={"link": link, "level": level, "title": title})
      total += int(created)
    logging.info(f"Created : {total} problems")
