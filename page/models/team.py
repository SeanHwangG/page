from ..common import logger, categories
from collections import defaultdict
from functools import lru_cache
from itertools import islice
from user.models import User


class Team:
  def __init__(self, team_id="", admin_ids=None, member_ids=None):
    self.team_id = team_id
    self.admin_ids = admin_ids or []
    self.member_ids = member_ids or []


if __name__ == "__main__":
  Team.show_progress("prake")
  # print(show_pro)
