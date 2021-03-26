from django.db import models


class Problem(models.Model):
  problem_id = models.CharField(max_length=255, null=False, primary_key=True)
  level = models.FloatField(default=-1)
  link = models.CharField(max_length=255, default="")
  title = models.CharField(max_length=255, default="")
  category_id = models.CharField(max_length=255, default="")
  solution_link = models.CharField(max_length=255, default="")

  class Meta:
    ordering = ['level']


class ProblemSite(models.Model):
  problem_site_id = models.CharField(max_length=255, primary_key=True)
  link = models.CharField(max_length=255, default="")
