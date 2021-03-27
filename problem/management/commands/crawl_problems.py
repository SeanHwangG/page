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
from markdown.models import Markdown, Header


class Command(BaseCommand):
  help = 'Update problem level'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_id', type=str, help="glob path for problems", choices=["BJ", "LC"])
    parser.add_argument('-l', '--limit', type=int, help="maximum number to parse -1 for all", default=None)
    parser.add_argument('-lv', '--level', type=int, help="only parse specific level", default=None)
    parser.add_argument('-nt', '--n_thread', action="store_true", help="Whether to parse problems in multithreading (default all available)", default=None)

  def handle(self, *args, **options):
    logging.info(f"{options}")
    site = Site.objects.get(site_id=options["site_id"])
    for problem_dic in crawl_problems(options["site_id"], options["limit"], options["level"], options["n_thread"]):
      Problem.objects.update_or_create(problem_id=problem_dic["problem_id"], defaults={"link": problem_dic["link"], "level": problem_dic["level"], "site": site, "title": problem_dic["title"]})
