from .base import *  # noqa

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
DEBUG = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

INSTALLED_APPS += ['django_extensions']
