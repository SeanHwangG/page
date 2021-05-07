import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from classroom.user.models import User


class Tag(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=255, default="", null=False)
  type = models.CharField(max_length=255, default="", null=False)

  def __str__(self):
    return f"{self.type}/{self.name}"

  class Meta:
    ordering = ['type', "name"]


class Site(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  code = models.CharField(max_length=255, null=False)
  name = models.CharField(max_length=255, default="", null=False)
  link = models.CharField(max_length=255, default="")

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ["name"]


class Account(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=255, default="")
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  site = models.ForeignKey(Site, null=False, on_delete=models.PROTECT)


class Problem(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  code = models.CharField(max_length=255, null=False)
  raw_level = models.CharField(max_length=255, default="")
  level = models.IntegerField(default=-1)
  link = models.CharField(max_length=255, default="")
  title = models.CharField(max_length=255, default="")
  tags = models.ManyToManyField(Tag)
  site = models.ForeignKey(Site, null=False, default="", on_delete=models.PROTECT)

  @property
  def user_with_solution_count(self):
    return len(Solution.objects.filter(problem=self))

  def __str__(self):
    return f"{self.code}"

  class Meta:
    ordering = ['level', 'code']


class Solution(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  problem = models.ForeignKey(Problem, null=False, on_delete=models.CASCADE)
  link = models.CharField(max_length=255, default="")
  language = models.CharField(max_length=255, null=False, default="unknown",
                              choices=[("python", "python"), ("c++", "c++"), ("java", "java"),
                                       ("shell", "shell"), ("sql", "sql"), ("go", "go"), ("unknown", "unknown")])
  code = models.CharField(max_length=65535, default="")

  def __str__(self):
    return f"{problem} by {user}"

  class Meta:
    ordering = ["-created"]
