import uuid
from django.db import models
from user.models import User
from datetime import datetime


class Tag(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=255, null=False)
  group = models.CharField(max_length=255, null=False, choices=[("syntax", "syntax"), ("algorithm", "algorithm"), ("sql", "sql"), ("type", "type")])
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.group} {self.name}"

  class Meta:
    ordering = ['group', "name"]


class Site(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  code = models.CharField(max_length=255, null=False)
  name = models.CharField(max_length=255, default="", null=False)
  link = models.CharField(max_length=255, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ["name"]


class Account(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  login_id = models.CharField(max_length=255, default="")
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  site = models.ForeignKey(Site, null=False, on_delete=models.PROTECT)


class Problem(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=255, null=False)
  level = models.IntegerField(default=-1)
  link = models.CharField(max_length=255, default="")
  title = models.CharField(max_length=255, default="")
  tags = models.ManyToManyField(Tag)
  site = models.ForeignKey(Site, null=False, default="", on_delete=models.PROTECT)
  list_display = ['name', 'level']
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  @property
  def user_with_solution_count(self):
    return len(Solution.objects.filter(name=self.name))

  def __str__(self):
    return f"{self.name}"

  class Meta:
    ordering = ['level', 'name']


class Solution(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  problem = models.ForeignKey(Problem, null=False, on_delete=models.PROTECT)
  link = models.CharField(max_length=255, default="")
  language = models.CharField(max_length=255, null=False, default="unknown",
                              choices=[("python", "python"), ("c++", "c++"), ("java", "java"),
                                       ("shell", "shell"), ("sql", "sql"), ("go", "go"), ("unknown", "unknown")])
  code = models.CharField(max_length=65535, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-created_at"]
