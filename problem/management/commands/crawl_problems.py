import io
import logging
import yaml
import pathlib
import panflute
import re
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from util.crawler import crawl_problems
from problem.models import Tag, Problem, Site


class Command(BaseCommand):
  help = 'Update problem level'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_id', type=str, help="glob path for problems", choices=["BJ", "LC", "KT"])
    parser.add_argument('-nt', '--n_thread', type=int, help="Whether to parse problems in multithreading (default all available)", default=None)
    parser.add_argument('-t', '--test', help="Only parse few problems for testing", action="store_true")

  def handle(self, *args, **options):
    logging.info(f"{options}")
    site = Site.objects.get(site_id=options["site_id"])
    for problem_dic in crawl_problems(options["site_id"], options["n_thread"], options["test"]):
      Problem.objects.update_or_create(problem_id=problem_dic["problem_id"], link=problem_dic["link"], level=problem_dic["level"], site_id=options["site_id"], title=problem_dic["title"])
