from django.db import models
from problem.models import Problem
from user.models import User


class Solution(models.Model):
  solution_id = models.TextField(max_length=255, null=False, primary_key=True)
  problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  language = models.TextField(max_length=255, null=True)
  text = models.TextField(max_length=65535, null=True)
