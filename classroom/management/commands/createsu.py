from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
  def handle(self, *args, **options):
    admin_ids = os.environ.get("DJANGO_ADMINS").split(",")
    admin_pws = os.environ.get("DJANGO_PASSWORDS").split(",")
    admin_emails = os.environ.get("DJANGO_EMAILS").split(",")
    for admin_id, admin_pw, admin_email in zip(admin_ids, admin_pws, admin_emails):
      if not User.objects.filter(username=admin_id).exists():
        User.objects.create_superuser(admin_id, admin_email, admin_pw)
