import io
import logging
from pathlib import Path
import re
import traceback
import panflute
import yaml
from operator import itemgetter
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from problem.models import Solution, Problem, Site, Tag, Account
from user.models import Membership, User, Team
from util.crawler import crawl_solutions


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_code', type=str, help="Type of problem site_id", choices=["BJ"], required=True)
    parser.add_argument('-t', '--team_name', type=str, help="team_name")
    parser.add_argument('-u', '--user_name', type=str, help="user_name")
    parser.add_argument('-nt', '--n_thread', action="store_true", help="Number of thread to parse solutions (default all available)", default=None)

  def handle(self, *args, site_code: str = None, team_name: str = None, user_name: str = None, n_thread: int = None, **options):
    logging.info(f"handle({site_code}, {team_name}, {user_name}, {n_thread})")
    assert not (team_name and user_name), "Wrong Params : Please only use team_name or user_name"
    try:
      if team_name:
        team = Team.objects.get(name=team_name)
        users = User.objects.filter(membership__team=team)
      elif user_name:
        users = User.objects.filter(name=user_name)
      site = Site.objects.get(code=site_code)
      account_names = [Account.objects.get(user=user, site=site).name for user in users]
      solution_dics = crawl_solutions(account_names, site.code, n_thread)
      for user, solution_dic in zip(users, solution_dics):
        unseen_total, seen_total = 0, 0
        account_name, problem_codes = itemgetter("account_name", "problem_codes")(solution_dic)
        for problem_code in problem_codes:
          problem, unseen_created = Problem.objects.get_or_create(code=problem_code, site=site)
          _, seen_created = Solution.objects.update_or_create(user=user, problem=problem)
          unseen_total, seen_total = unseen_total + int(unseen_created), seen_total + int(seen_created)
        logging.info(f"Created : {unseen_total} new problems, {seen_total} solutions by {user.name} solved")

    except Exception as e:
      logging.error(traceback.format_exc())
