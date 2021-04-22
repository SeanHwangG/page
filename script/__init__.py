import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "classroom.settings"
django.setup()

from django.conf import settings
from dotenv import load_dotenv

load_dotenv(settings.ENV_PATH)
