from django.core.management import call_command
from django.conf import settings
from django.test import TestCase
from io import StringIO


class GitbookTest(TestCase):
  def test_parsing(self):
    out = StringIO()
    call_command("parse_gitbook", stdout=out, default=f"{settings.NOTE_DIR}")
    self.assertContains(out.getvalue, "SUCCESS")
