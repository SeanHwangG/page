import logging
from django.conf import settings
from problem.models import Problem
from rest_framework.test import APITestCase
from common.util import get_chrome_driver


class AllTest(APITestCase):
  def setUp(self):
    self.browser = get_chrome_driver()

  def test_create_problem(self):
    initial_problem_count = Problem.objects.count()
    test_problem = {
        "problem_id": "TC_1234"
    }
    response = self.client.post("/problem/new", test_problem)
    if response.status_code != 201:
      logging.warning(response.data)

  def test_running(self):
    # self.browser.get("http://localhost:8000")
    pass
