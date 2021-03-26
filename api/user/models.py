from django.db import models
from team.models import Team


class User(models.Model):
  user_id = models.TextField(max_length=255, null=False, default="", primary_key=True)
  baekjoon_id = models.TextField(max_length=255, null=True)
  name = models.TextField(max_length=255, null=True)

  def __str__(self):
    return f"{self.name}"


class Membership(models.Model):
  TYPE = [("member", "MEMBER"), ("admin", "ADMIN")]
  membership_type = models.CharField(choices=TYPE, max_length=255, default="member")
  team_id = models.ForeignKey(Team, null=False, on_delete=models.PROTECT)
  user_id = models.ForeignKey(User, null=False, on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.user_id} is {self.team_id}'s {self.membership_type}"
