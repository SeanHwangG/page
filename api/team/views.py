from .models import Team
from django.shortcuts import render
from .models import Team


def home(request):
  context = {
      'teams': Team.objects.all()
  }
  return render(request, 'team/home.html', context)


"""
def show_progress(team_id):
  # for user in User.objects.filter(membership__team_id="prake"):
  memebers = [member for member in members if member.kr_name not in Team.NO_MORE]
  members.sort(key=lambda member: len(member.solved_problem_ids))
  html = '<div id="search-problem" onchange=toggle_visibility()>'
  html += 'bj_range=<input type="number" class="min_bj_level" value="1">~<input type="number" class="max_bj_level" value="10"><br>'

  for i, member in enumerate(reversed(members)):
    html += f'<input id="{member.id}" class="show_member_id" type="checkbox">{member.kr_name} {len(member.solved_problem_ids)} {member.baekjoon_id}</input><br>'
    member.solved_problem_ids = set(member.solved_problem_ids)

  problems = local_db.get_all("problem")
  problems = problems.values()
  cate2problems = defaultdict(list)
  for problem in problems:    # cache headers to problem for effeciency
    if problem.solution_link != "" and problem.problem_id.startswith("BJ"):
      cate2problems[f"{problem.category_id}"].append(problem)
  for category in categories:
    html += f"<h1>{category}</h1>"
    for problem in sorted(cate2problems[f"{category}"], key=lambda problem: problem.level):
      html += '<table style="table-layout:fixed;">'
      html += f"<tr id='{problem.level}' class='bj_level'>"
      html += f"<td style='width:400px;'>{problem.link}</td>"
      html += f"<td style='width:70px;'>{problem.solution_link}</td>"
      html += " ".join([f"< td > <span id={member.id} class='{'' if problem.problem_id in member.solved_problem_ids else 'member_id'}' \
                                                      style='display: none; '> {member.kr_name} < /span > </td >" for member in members])
      html += "</tr>"
    html += "</table>"
  html += "</div>"
  return html
"""
