from .database import local_db, remote_db
from .models.doc import Doc
from .models.member import Member
from .models.problem import Problem
from .common import PATH, logger
import json

# Member.update_all_baekjoon_solved([member for member in remote_db.get_all("member").values() if len(member.baekjoon_id) != 0])

# get docs from docs.json
# local_db.add("problem", Problem.get_baekjoon_problems() + Problem.get_leetcode_problems())

Member.update_all_baekjoon_solved([member for member in remote_db.get_all("member").values() if len(member.baekjoon_id) != 0])

problems = local_db.get_all("problem")
for document_path in sorted(PATH.PROBLEM.iterdir(), key=lambda a: h1s.index(a.stem)):
  for problem_path in document_path.iterdir():
    if problem_path.is_dir():
      continue
    with open(problem_path, "r") as f:
      try:
        category = document_path.stem   # operation
        problem = problem_path.stem     # BJ_1234
        problem = local_db.get('problem', problem_path.stem)
        problem.category_id = document_path.stem
        problem.solution_link = f'<a href="https://github.com/SeanHwangG/private/blob/main/practice/{category}/{problem}.md" style="color:blue;">solution</a>'
        local_db.add('problem', problem, True)
      except Exception as e:
        logger.info(e)
