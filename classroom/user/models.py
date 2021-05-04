import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Team(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=20, null=False)

  def __str__(self):
    return f"{self.name}"


class User(AbstractUser, TimeStampedModel):
  username = None
  first_name = None
  last_name = None

  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  email = models.EmailField(max_length=255, null=False, unique=True)
  name = models.TextField(max_length=255, null=True)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["password"]

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ['name']


class Membership(TimeStampedModel):
  TYPE = [("member", "MEMBER"), ("admin", "ADMIN")]
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  membership_type = models.CharField(choices=TYPE, max_length=255, default="member")
  team = models.ForeignKey(Team, null=False, default="", on_delete=models.PROTECT)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.user} is {self.team}'s {self.membership_type}"

  class Meta:
    ordering = ['user']
