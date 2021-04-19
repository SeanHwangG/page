import uuid
from django.db import models
from user.models import User
from datetime import datetime


class Tag(models.Model):
  tag_id = models.CharField(max_length=255, null=False, primary_key=True)
  group = models.CharField(max_length=255, null=False, choices=[("syntax", "syntax"), ("algorithm", "algorithm"), ("sql", "sql"), ("type", "type")])
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.group} {self.tag_id}"

  class Meta:
    ordering = ['group', "tag_id"]


class Site(models.Model):
  site_id = models.CharField(max_length=255, null=False, primary_key=True)
  name = models.CharField(max_length=255, default="", null=False)
  link = models.CharField(max_length=255, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["site_id"]


class Problem(models.Model):
  problem_id = models.CharField(max_length=255, null=False, primary_key=True)
  level = models.IntegerField(default=-1)
  link = models.CharField(max_length=255, default="")
  title = models.CharField(max_length=255, default="")
  tags = models.ManyToManyField(Tag)
  site = models.ForeignKey(Site, null=False, default="", on_delete=models.PROTECT)
  list_display = ['problem_id', 'level']
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  @property
  def user_with_solution_count(self):
    return len(Solution.objects.filter(problem_id=self.problem_id))

  def __str__(self):
    return f"{self.problem_id}"

  class Meta:
    ordering = ['level']


class Solution(models.Model):
  solution_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
  problem = models.ForeignKey(Problem, null=False, on_delete=models.PROTECT)
  link = models.CharField(max_length=255, default="")
  language = models.CharField(max_length=255, null=False, default="unknown",
                              choices=[("python", "python"), ("c++", "c++"), ("java", "java"),
                                       ("shell", "shell"), ("sql", "sql"), ("go", "go"), ("unknown", "unknown")])
  code = models.CharField(max_length=65535, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
