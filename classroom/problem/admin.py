import logging

from admin_numeric_filter.admin import RangeNumericFilter, SliderNumericFilter
from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.utils.html import format_html

from .models import Account, Problem, Site, Solution, Tag


class AccountAdmin(admin.ModelAdmin):
  list_display = ("user", "site", "name")


class TagAdmin(admin.ModelAdmin):
  list_display = ("name", "type", "modified",)


class CustomSliderNumericFilter(SliderNumericFilter):
  MAX_DECIMALS = 2
  STEP = 10


class ProblemAdmin(admin.ModelAdmin):
  list_display = ("code", "title_link", "tag_list", "solved_users", "created", "user_with_solution_count")
  list_filter = ("site__name", "tags", "created", ("level", RangeNumericFilter),)
  search_fields = ('code', "title")
  list_per_page = 500

  def get_queryset(self, request):
    qs = super(ProblemAdmin, self).get_queryset(request)
    qs = qs.annotate(solved_by=models.Count("solution"))
    return qs

  def title_link(self, problem):
    return format_html(f"<a href={problem.link}>[{problem.raw_level}] {problem.title}</a>")

  def tag_list(self, problem):
    return "\n".join([t.name for t in problem.tags.all()])

  def solved_users(self, problem):
    solutions = Solution.objects.filter(problem=problem).order_by("user")
    return format_html(", ".join(f"<a href={solution.link}>{solution.user}</a>" if solution.link else str(solution.user) for solution in solutions))


class SolutionAdmin(admin.ModelAdmin):
  list_display = ("user", "problem", "language", "created", "link")
  list_filter = ("user", "language", "created")
  list_editable = ("language",)
  search_fields = ("problem__code",)
  list_per_page = 500


class SiteAdmin(admin.ModelAdmin):
  list_display = ("name", "site_link", "total_problem", "name", "modified")

  def get_queryset(self, request):
    qs = super(SiteAdmin, self).get_queryset(request)
    qs = qs.annotate(total_problems=models.Count("problem"))
    return qs

  def total_problem(self, user):
    return user.total_problems

  def site_link(self, site):
    return format_html(f"<a href={site.link}>{site.link}</a>")


admin.site.register(Account, AccountAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Solution, SolutionAdmin)
