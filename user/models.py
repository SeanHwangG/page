import uuid
from django.db import models


class Team(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=20, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"


class User(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  email = models.TextField(max_length=255, null=False)
  name = models.TextField(max_length=255, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ['name']


class Membership(models.Model):
  TYPE = [("member", "MEMBER"), ("admin", "ADMIN")]
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  membership_type = models.CharField(choices=TYPE, max_length=255, default="member")
  team = models.ForeignKey(Team, null=False, default="", on_delete=models.PROTECT)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user} is {self.team}'s {self.membership_type}"

  class Meta:
    ordering = ['user']
