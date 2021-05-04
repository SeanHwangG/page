from django.contrib import admin

from .models import File, Repository

admin.site.register(File)
admin.site.register(Repository)
