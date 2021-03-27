from django.contrib import admin
from django.utils.html import format_html
import logging

from .models import Tag, Problem, Site, Solution


class TagAdmin(admin.ModelAdmin):
  list_display = ("group", "tag_id", "modified_at",)
  list_editable = ("tag_id",)


class ProblemAdmin(admin.ModelAdmin):
  list_display = ("problem_id", "title_link", "tag_list", "solved_students", "created_at")
  list_filter = ("site__site_id", "tags", "created_at")
  search_fields = ('problem_id', "title")
  list_per_page = 500

  def title_link(self, problem):
    return format_html(f"<a href={problem.link}>[{int(problem.level)}] {problem.title}</a>")

  def tag_list(self, problem):
    return "\n".join([t.tag_id for t in problem.tags.all()])

  def solved_students(self, problem):
    solutions = Solution.objects.filter(problem=problem).order_by("user")
    return format_html(", ".join(f"<a href={solution.link}>{solution.user.name}</a>" if solution.link else solution.user.name for solution in solutions))


class SolutionAdmin(admin.ModelAdmin):
  list_display = ("problem_id", "user_id", "language", "created_at")
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
