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
from classroom.problem.models import Solution, Problem, Site, Tag, Account
from classroom.user.models import Membership, User, Team
from classroom.util.crawler import crawl_solutions


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-s', '--site_code', type=str, help="Type of problem site_id", choices=["BJ"], required=True)
    parser.add_argument('-t', '--team_name', type=str, default="", help="team_name")
    parser.add_argument('-u', '--user_name', type=str, default="", help="user_name")
    parser.add_argument('-nt', '--n_thread', action="store_true",
                        help="Number of thread to parse (default available)", default=None)

  def handle(self, site_code: str, team_name: str, user_name: str, n_thread: int, *args, **options):
    logging.info("handle(%s, %s, %s, %s)", site_code, team_name, user_name, n_thread)
    assert not (team_name and user_name), "Wrong Params : Please only use team_name or user_name"
    if team_name:
      team = Team.objects.get(name=team_name)
      users = User.objects.filter(membership__team=team)
    elif user_name:
      users = User.objects.filter(name=user_name)
    site = Site.objects.get(code=site_code)
    account_name2user = {Account.objects.get(user=user, site=site).name: user for user in users}
    solution_dics = crawl_solutions(account_name2user.keys(), site.code, n_thread)
    for solution_dic in solution_dics:
      user = account_name2user[solution_dic["account_name"]]
      unseen_total, seen_total = 0, 0
      account_name, problem_codes = itemgetter("account_name", "problem_codes")(solution_dic)
      for problem_code in problem_codes:
        problem, unseen_created = Problem.objects.get_or_create(code=problem_code, site=site)
        _, seen_created = Solution.objects.get_or_create(user=user, problem=problem)
        if unseen_created:
          unseen_total += 1
          logging.debug("Created : %s by %s", problem, user)
        if seen_created:
          seen_total += 1
          logging.debug("Solved : %s by %s", problem, user)
      logging.info("Created : %s new problems, %s solutions by %s solved", unseen_total, seen_total, user)
