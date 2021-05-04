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
  SITE_CHOICES = ["BJ", "CC", "CF", "LC", "KT", "HR"]

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_code', type=str, help="glob path for problems",
                        choices=["all", *self.SITE_CHOICES])
    parser.add_argument('-nt', '--n_thread', type=int, help="numer of thread to crawl (default all)", default=None)

  def crawl_problems(self, site_code, n_thread):
    site = Site.objects.get(code=site_code)
    total = 0

    # Only crawl problems within our database
    if site_code == "HR":
      problem_codes = list(Problem.objects.filter(code="HR").values_list('code', flat=True))
    elif site_code == "CC":
      problem_codes = list(Problem.objects.filter(code="CC").values_list('code', flat=True))
    else:
      problem_codes = None

    for problem_dic in crawl_problems(site_code, n_thread, problem_codes):
      link, problem_code, level, title = itemgetter("link", "problem_code", "level", "title")(problem_dic)
      _, created = Problem.objects.update_or_create(site=site, code=problem_code, defaults={
                                                    "link": link, "level": level, "title": title})
      total += int(created)
    logging.info("Created : %s problems", total)

  def handle(self, site_code: str = None, n_thread: int = None, *args, **options):
    logging.info("handle(%s, %s)", site_code, n_thread)

    if site_code == "all":
      for site_code in self.SITE_CHOICES:
        self.crawl_problems(site_code, n_thread)
    else:
      self.crawl_problems(site_code, n_thread)
