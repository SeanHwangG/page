from rest_framework.test import APITestCase
import logging


class AllTest(APITestCase):
  def setUp(self):
    pass

  def test_create_problem(self):
    initial_problem_count = Problem.objects.count()
    for user in users:
      response = self.client.post("/user/new", user, format="json")
      if response.status_code != 201:
        logging.warning(response.data)

  def test_running(self):
    # self.browser.get("http://localhost:8000")
    pass
