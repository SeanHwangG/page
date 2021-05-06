import os

import django
from django.conf import settings
from dotenv import load_dotenv

os.environ["DJANGO_SETTINGS_MODULE"] = "classroom.settings.local"
django.setup()


load_dotenv(settings.ENV_PATH)
