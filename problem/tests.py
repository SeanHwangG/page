import logging
from django.conf import settings
from problem.models import Problem
from rest_framework.test import APITestCase
from util.driver import get_chrome_driver


class AllTest(APITestCase):
  def setUp(self):
    self.browser = get_chrome_driver()

  def test_create_problem(self):
    pass

  def test_running(self):
    # self.browser.get("http://localhost:8000")
    pass
