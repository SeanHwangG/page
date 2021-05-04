import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice
from threading import local
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

thread_local = local()


def get_chrome_driver(headless=True):
  driver = getattr(thread_local, 'driver', None)
  if driver is None:
    chrome_options = webdriver.ChromeOptions()
    if headless:
      chrome_options.add_argument('--headless')  # TODO Headless doesn't work for hackerrank
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    setattr(thread_local, 'driver', driver)
  return driver


def _crawl_BJ_solutions(account_name: str) -> Dict:
  logging.info("_crawl_BJ_solutions(%s)", account_name)
  driver = get_chrome_driver()
  driver.get(f"https://www.acmicpc.net/user/{account_name}")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
  return [{"account_name": account_name,
           "problem_codes": [problem for problem in driver.find_element_by_class_name('panel-body').text.split()]}]


def _crawl_BJ_problems_level(level):
  logging.debug("_crawl_BJ_problems_level(%s)", level)
  driver = get_chrome_driver()
  problems = []
  for page in range(1, 100):
    driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
    lines = driver.find_element_by_class_name('contents').text
    if '해당하는 문제가 없습니다' in lines:
      break
    for line in lines.split("\n"):          # ex)
      line = line.strip("STANDARD").strip()  # 10430 나머지 계산 STANDARD -> 10430 나머지 계산
      code_title = line.split(' ', 1)       # 10430 나머지 계산 -> [10430, 나머지 계산]
      if code_title[0].isdigit() and len(code_title) == 2:
        code, title = code_title
        link = f'http://acmicpc.net/problem/{code}'
        problems.append({"site_code": "BJ",
                         "problem_code": code,
                         "link": link,
                         "level": level,
                         "title": title})
  return problems


def _crawl_LC_problems(limit: int = None):
  logging.info("_crawl_LC_problems(%s)", limit)
  driver = get_chrome_driver()
  problems = []
  driver.get(f"https://leetcode.com/problemset/all/")
  select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'select'))))
  select.select_by_visible_text('all')
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

  data = driver.find_element_by_class_name("reactable-data").find_elements_by_tag_name("tr")
  for prob in islice(data, limit):
    code, title, level = prob.text.split('\n')
    problems.append({"site_code": "LC",
                     "problem_code": code,
                     "level": {"Easy": 1, "Medium": 2, "Hard": 3}[level[level.find(' ') + 1:]],
                     "link": prob.find_element_by_css_selector("a").get_attribute('href'),
                     "title": title.strip()})
  return problems


def _crawl_KT_problems_page(page: int):
  logging.info("_crawl_KT_problems_page(%s)", page)
  driver = get_chrome_driver()
  problems = []
  driver.get(f"https://open.kattis.com/problems?page={page}")
  for row_tag in driver.find_elements_by_css_selector("tr.odd,tr.even"):
    title, _, _, _, _, _, _, _, level = row_tag.text.rsplit(maxsplit=8)
    link = row_tag.find_element_by_css_selector("a").get_attribute('href')
    problems.append({"site_code": "KT",
                     "problem_code": f"{link.rsplit('/')[-1]}",
                     "title": title,
                     "link": link,
                     "level": level})
  return problems


def _crawl_CC_problem(code: str):
  logging.info("_crawl_CC_problems(%s)", code)
  CC_levels = ["", "Beginner", "Easy", "Medium", "Hard", "Challenge", "Extcontest"]
  driver = get_chrome_driver()
  link = f"https://www.codechef.com/problems/{code}"
  level = CC_levels.index(driver.find_elements_by_css_selector("aside>a")[1].text[9:-1])
  driver.get(link)
  return {"site_code": "CC",
          "problem_code": code,
          "title": driver.find_element_by_css_selector("h1").text.split(" Problem Code")[0],
          "link": link,
          "level": level}


def _crawl_CF_problems_page(page: int):
  logging.info("_crawl_CF_problems_page(%s)", page)
  driver = get_chrome_driver()
  problems = []
  driver.get(f"https://codeforces.com/problemset/page/{page}")
  for row_tag in driver.find_elements_by_css_selector("table.problems>tbody>tr")[1:]:
    if row_tag.text.count("\n") == 3:
      code, title, _, level = row_tag.text.split("\n")
    else:
      code, title, level = row_tag.text.split("\n")
    level = next(iter(re.findall(r"\d+", level)), -1)
    link = row_tag.find_element_by_css_selector("a").get_attribute('href')
    problems.append({"site_code": "CF",
                     "problem_code": f"{code}",
                     "title": title,
                     "link": link,
                     "level": level})
  return problems


def _crawl_HR_problem(code: str):
  logging.info("_crawl_HR_problem({code})")
  driver = get_chrome_driver(False)
  link = f"https://www.hackerrank.com/challenges/{code}/problem"
  logging.info(link)
  driver.get(link)
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'difficulty-block')))
  level = driver.find_elements_by_class_name("difficulty-block")[1].text.split()[-1]
  return {"site_code": "HR",
          "problem_code": code,
          "link": link,
          "title": driver.find_element_by_class_name("ui-icon-label").text,
          "level": {"Easy": 1, "Medium": 2, "Hard": 3}[level]}


def crawl_problems(site_id: str, n_thread: int = None, codes: List[str] = None):
  """ Return generator of problem DTO """
  logging.debug("crawl_problems(%s, %s)", site_id, n_thread)
  assert not n_thread or site_id in ["BJ", "KT"], "n_thread only supports in BJ, KT"
  if site_id == "LC":   # no multithread yet TODO
    yield from _crawl_LC_problems()
  else:  # multithread by level
    with ThreadPoolExecutor(n_thread) as ex:
      if site_id == "BJ":
        futures = [ex.submit(_crawl_BJ_problems_level, level) for level in range(31)]
      elif site_id == "KT":  # TODO, remove hardcode
        futures = [ex.submit(_crawl_KT_problems_page, page) for page in range(50)]
      elif site_id == "CF":  # multithread by page
        futures = [ex.submit(_crawl_CF_problems_page, page) for page in range(80)]
      # Multithread by question
      elif site_id == "HR":
        futures = [ex.submit(_crawl_HR_problem, code) for code in codes]
      elif site_id == "CC":
        futures = [ex.submit(_crawl_CC_problem, code) for code in codes]
      else:
        raise Exception(f"Unknown site : {site_id}")
      for future in as_completed(futures):
        problem = future.result()
        if problem:
          yield from problem


def crawl_solutions(account_names: str, site_id: str, n_thread: int = None):
  logging.info("crawl_solutions(%s, %s)", account_names, site_id)
  if site_id == "BJ":
    with ThreadPoolExecutor(n_thread) as ex:
      future2level = [ex.submit(_crawl_BJ_solutions, account_name) for account_name in account_names]
      for future in as_completed(future2level):
        yield from future.result()
