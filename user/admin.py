from django.contrib import admin
from django.db import models
from .models import User, Membership, Team
from problem.models import Solution
import logging


class UserAdmin(admin.ModelAdmin):
  list_display = ("name", "BJ_id", "BJ_count", "created_at")

  def get_queryset(self, request):
    qs = super(UserAdmin, self).get_queryset(request)
    qs = qs.annotate(BJ_solution_count=models.Count("solution"))
    return qs

  def BJ_count(self, user):
    return user.BJ_solution_count
  BJ_count.admin_order_field = "BJ_solution_count"


class MembershipAdmin(admin.ModelAdmin):
  list_display = ("user", "team", "membership_type")


class TeamAdmin(admin.ModelAdmin):
  list_display = ("team_id", "team_admin", "created_at")

  def team_admin(self, team):
    return ",".join(Membership.objects.filter(team=team, membership_type="admin").values_list('user__name', flat=True))


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Membership, MembershipAdmin)
