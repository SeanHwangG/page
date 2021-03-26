from django.contrib import admin

from .models import User, Membership

admin.site.register(User)
admin.site.register(Membership)
