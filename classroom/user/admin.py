from django.contrib import admin
from django.db import models
from django.db.models import Q
from .models import User, Membership, Team
from classroom.problem.models import Solution
import datetime
import logging


class UserAdmin(admin.ModelAdmin):
  list_display = ("name", "all_count", "today_count", "created")

  def get_queryset(self, request):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    qs = super(UserAdmin, self).get_queryset(request)
    qs = qs.annotate(BJ_solution_count=models.Count("solution"))
    qs = qs.annotate(BJ_today_solution_count=models.Count("solution", filter=Q(solution__created__gt=yesterday)))
    return qs

  def today_count(self, user):
    return user.BJ_today_solution_count

  def all_count(self, user):
    return user.BJ_solution_count

  all_count.admin_order_field = "BJ_solution_count"


class MembershipAdmin(admin.ModelAdmin):
  list_display = ("user", "team", "membership_type")
  exclude = ("membership_id",)


class TeamAdmin(admin.ModelAdmin):
  list_display = ("name", "team_admin", "created")

  def team_admin(self, team):
    return ",".join(Membership.objects.filter(team=team, membership_type="admin").values_list('user__name', flat=True))


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Membership, MembershipAdmin)
