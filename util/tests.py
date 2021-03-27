from django.test import TestCase
from django.conf import settings
from .driver import get_chrome_driver


class AllTest(TestCase):
  def setUp(self):
    self.browser = get_chrome_driver()

  def test_path(self):
    for path in dir(settings):
      if path.endswith('_DIR') and getattr(settings, path):
        self.assertTrue(getattr(settings, path).is_dir())

  def test_running(self):
    # self.browser.get("http://localhost:8000")
    pass
