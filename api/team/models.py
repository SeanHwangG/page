from collections import defaultdict
from functools import lru_cache
from itertools import islice
from django.db import models


class Team(models.Model):
  team_id = models.CharField(max_length=20, null=False, primary_key=True)

  def __str__(self):
    return f"{self.team_id}"
