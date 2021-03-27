from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserSerializer
from .models import User, Membership
from problem.models import Problem, Tag, Solution
from django.http import HttpResponse


def user(request):
  context = User.objects.get(name="황규승")
  return render(request, "user/home.html", {"user": context.__dict__})


class UserList(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserCreate(CreateAPIView):
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)


def show_progress(team_id):
  users = User.objects.filter(membership__team_id="prake", membership__membership_type="member")
  problems = Problem.objects.all()
  html = '<div id="search-problem" onchange=toggle_visibility()>'
  html += 'bj_range=<input type="number" class="min_bj_level" value="1">~<input type="number" class="max_bj_level" value="10"><br>'

  for i, user in enumerate(users):
    html += f'<input id="{user.user_id}" class="show_member_id" type="checkbox">{user.name} {user.BJ_id}</input><br>'

  for tag in Tag.objects.all():
    html += f"<h1>{tag.tag_id}</h1>"
    for problem in Problem.objects.filter(tags__tag_id=tag.tag_id):
      html += '<table style="table-layout:fixed;">'
      html += f"<tr id='{problem.level}' class='bj_level'>"
      html += f"<td style='width:400px;'>{problem.link}</td>"
      html += f"<td style='width:70px;'>{Solution.objects.get(problem_id=problem).link}</td>"
      for user in users:
        html += f" <td> <span id={user.user_id} class={'' if Solution.objects.filter(user_id = user.user_id, problem_id=problem.problem_id) else user.user_id} style='display: none;'> {user.name} </span> </td>"
      html += "</tr>"
    html += "</table>"
  html += "</div>"
  return HttpResponse(html)
