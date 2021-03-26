from .database import local_db, remote_db
from .models.doc import Doc
from .models.member import Member
from .models.problem import Problem
from .common import PATH, logger, categories
import traceback
import json


# get docs from docs.json
# local_db.add("problem", Problem.get_baekjoon_problems() + Problem.get_leetcode_problems())
members = remote_db.get_all("member")
logger.info(members)
Member.update_all_baekjoon_solved([member for member in members.values() if len(member.baekjoon_id) != 0])
# document_paths = sorted(list(PATH.PROBLEM.iterdir()), key=lambda a: categories.index(a.stem) if a.stem in categories else float("inf"))
# for document_path in document_paths:
#   logger.info(document_path)
#   for problem_path in document_path.iterdir():
#     if problem_path.is_dir():
#       continue
#     with open(problem_path, "r") as f:
#       category = document_path.stem   # operation
#       problem = problem_path.stem     # BJ_1234
#       if problem_path.stem[:2] in ["KT", "HR"]:
#         continue
#       try:
#         problem = local_db.get('problem', problem_path.stem)
#         problem.category_id = document_path.stem
#         problem.solution_link = f'<a href="https://github.com/SeanHwangG/note/blob/main/book/embed/{category}/{problem}.md" style="color:blue;">solution</a>'
#         if local_db.add('problem', problem, True):
#           logger.debug(f"update {problem}")
#       except Exception as e:
#         var = traceback.format_exc()
#         logger.warn(var)
#
