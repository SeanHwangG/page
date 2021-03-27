import uuid
from django.db import models
from datetime import datetime


class Team(models.Model):
  team_id = models.CharField(max_length=20, null=False, primary_key=True)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.team_id}"


class User(models.Model):
  user_id = models.TextField(max_length=255, null=False, default="", primary_key=True)
  BJ_id = models.TextField(max_length=255, null=True)
  name = models.TextField(max_length=255, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ['name']


class Membership(models.Model):
  TYPE = [("member", "MEMBER"), ("admin", "ADMIN")]
  membership_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  membership_type = models.CharField(choices=TYPE, max_length=255, default="member")
  team = models.ForeignKey(Team, null=False, default="", on_delete=models.PROTECT)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user} is {self.team}'s {self.membership_type}"

  class Meta:
    ordering = ['user']