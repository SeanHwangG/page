from django.contrib import admin
from django.db import models
from django.utils.html import format_html
import logging
from admin_numeric_filter.admin import RangeNumericFilter, SliderNumericFilter


from .models import Tag, Problem, Site, Solution


class TagAdmin(admin.ModelAdmin):
  list_display = ("tag_id", "group",  "modified_at",)


class CustomSliderNumericFilter(SliderNumericFilter):
  MAX_DECIMALS = 2
  STEP = 10


class ProblemAdmin(admin.ModelAdmin):
  list_display = ("problem_id", "title_link", "tag_list", "solved_users", "created_at", "user_with_solution_count")
  list_filter = ("site__site_id", "tags", "created_at")  # , ("level", RangeNumericFilter),)
  search_fields = ('problem_id', "title")
  list_per_page = 500

  def get_queryset(self, request):
    qs = super(ProblemAdmin, self).get_queryset(request)
    qs = qs.annotate(solved_by=models.Count("solution"))
    return qs

  def title_link(self, problem):
    return format_html(f"<a href={problem.link}>[{int(problem.level)}] {problem.title}</a>")

  def tag_list(self, problem):
    return "\n".join([t.tag_id for t in problem.tags.all()])

  def solved_users(self, problem):
    solutions = Solution.objects.filter(problem=problem).order_by("user")
    return format_html(", ".join(f"<a href={solution.link}>{solution.user.name}</a>" if solution.link else solution.user.name for solution in solutions))


class SolutionAdmin(admin.ModelAdmin):
  list_display = ("problem_id", "user_id", "language", "created_at", "link")
  list_filter = ("user", "language", "created_at")
  list_editable = ("language",)
  search_fields = ("problem__problem_id",)
  list_per_page = 500


class SiteAdmin(admin.ModelAdmin):
  list_display = ("site_id", "site_link", "modified_at",)

  def site_link(self, site):
    return format_html(f"<a href={site.link}>{site.link}</a>")


admin.site.register(Tag, TagAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Solution, SolutionAdmin)
