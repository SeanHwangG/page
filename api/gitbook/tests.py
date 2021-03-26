from django.core.management import call_command
from django.test import TestCase
from io import StringIO


class GitbookTest(TestCase):
  def test_parsing(self):
    out = StringIO()
    call_command("parse_gitbook", stdout=out)
    self.assertContains(out.getvalue, "SUCCESS")
