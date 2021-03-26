import json
import re
import os
from ..common import PATH, logger,  get_chrome_driver
from itertools import islice, chain
from firebase_admin import credentials, firestore, initialize_app
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Problem():
  def __init__(self, problem_id="", title="", level="", link="", category_id="", solution_link=""):
    self.problem_id = problem_id
    self.title = title
    self.level = level
    self.link = link
    self.category_id = category_id
    self.solution_link = solution_link

  def __repr__(self):
    return f"{self.problem_id}"

  def __str__(self):
    return f"{self.__dict__}"

  @classmethod
  def get_baekjoon_problems_level(cls, level):
    logger.debug(f"get_baekjoon_problems_level({level})")
    driver = get_chrome_driver()
    problems = []
    try:
      id_title = []
      for page in range(1, 100):
        driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
        logger.debug(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
        lines = driver.find_element_by_class_name('contents').text
        if '해당하는 문제가 없습니다' in lines:
          break
        for line in lines.split("\n"):                      # ex)
          line = line.strip("STANDARD").strip()             # 10430 나머지 계산 STANDARD -> 10430 나머지 계산
          id_title = line.split(' ', 1)                     # 10430 나머지 계산 -> [10430, 나머지 계산]
          if id_title[0].isdigit() and len(id_title) == 2:
            id, title = id_title
            problem_id = f"BJ_{id}"
            link = f'<a href="http://acmicpc.net/problem/{id}" style="color:blue;">{problem_id} {title} ({level})</a>'
            problem = cls(problem_id, title, level, link)
            problems.append(problem)
    except Exception as e:
      logger.warn(e)
    finally:
      driver.quit()
    return problems

  @classmethod
  def get_baekjoon_problems(cls, lo=0, hi=31):
    logger.debug(f"update_baekjoon_problems({lo}, {hi})")
    problems = []
    with ThreadPoolExecutor() as ex:
      future2level = {ex.submit(Problem.get_baekjoon_problems_level, level): level for level in range(lo, hi)}
      for future in as_completed(future2level):
        problems.extend(future.result())
    return problems

  @classmethod
  def get_leetcode_problems(cls, total_count=10000):
    logger.debug(f"update_leetcode({total_count})")
    driver = get_chrome_driver()
    problems = []

    try:
      driver.get(f"https://leetcode.com/problemset/all/")

      select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'select'))))
      select.select_by_visible_text('all')
      WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

      data = driver.find_element_by_class_name("reactable-data").find_elements_by_tag_name("tr")
      for prob in islice(data, total_count):
        id, title, level = prob.text.split('\n')
        level = {"Easy": 1, "Medium": 2, "Hard": 3}[level[level.find(' ') + 1:]]
        link = prob.find_element_by_css_selector("a").get_attribute('href')
        link = f'<a href="{link}" style="color:blue;">{title} ({level})</a>'
        problem = cls(f"LC_{id}", title, level, link)
        logger.debug(f"{id} {title}")
        problems.append(problem)
    except Exception as e:
      logger.error(e)
    finally:
      driver.quit()
    return problems
