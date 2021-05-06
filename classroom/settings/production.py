from .base import *  # noqa

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["ec2-3-37-19-71.ap-northeast-2.compute.amazonaws.com/"])

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            "IGNORE_EXCEPTIONS": True,
        },
    }
}
