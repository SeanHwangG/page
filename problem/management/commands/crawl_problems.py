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
    parser.add_argument('-s', '--site_id', type=str, help="glob path for problems", choices=["BJ", "LC", "KT", "HR"])
    parser.add_argument('-nt', '--n_thread', type=int, help="Whether to parse problems in multithreading (default all available)", default=None)

  def handle(self, *args, site_id=None, n_thread=None, **options):
    logging.info(f"handle({site_id}, {n_thread})")
    site = Site.objects.get(site_id=site_id)
    total = 0

    problem_ids = list(Problem.objects.filter(site_id="HR").values_list('problem_id', flat=True)) if site_id == "HR" else None

    for problem_dic in crawl_problems(site_id, n_thread, problem_ids):
      link, problem_id, level, title = itemgetter("link", "problem_id", "level", "title")(problem_dic)
      _, created = Problem.objects.update_or_create(problem_id=problem_id, defaults={"link": link, "level": level, "site_id": site_id, "title": title})
      total += int(created)
    logging.info(f"Created : {total} problems")
