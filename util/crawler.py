from threading import local
from django.conf import settings
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice

import traceback
import logging

thread_local = local()


def get_chrome_driver():
  driver = getattr(thread_local, 'driver', None)
  if driver is None:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless') TODO Headless doesn't work for hackerrank
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    setattr(thread_local, 'driver', driver)
  return driver


def _crawl_BJ_solutions(BJ_id):
  logging.info(f"_crawl_BJ_solutions({BJ_id})")
  driver = get_chrome_driver()
  try:
    driver.get(f"https://www.acmicpc.net/user/{BJ_id}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
    return [{"user_id": BJ_id,
             "problem_ids": [f"BJ_{problem}" for problem in driver.find_element_by_class_name('panel-body').text.split()]}]
  except Exception as e:
    logging.warning(f"{e}")
  finally:
    driver.quit()


def _crawl_BJ_problems_level(level):
  logging.debug(f"_crawl_BJ_problems_level({level})")
  driver = get_chrome_driver()
  problems = []
  try:
    for page in range(1, 100):
      driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
      lines = driver.find_element_by_class_name('contents').text
      if '해당하는 문제가 없습니다' in lines:
        break
      for line in lines.split("\n"):          # ex)
        line = line.strip("STANDARD").strip()  # 10430 나머지 계산 STANDARD -> 10430 나머지 계산
        id_title = line.split(' ', 1)         # 10430 나머지 계산 -> [10430, 나머지 계산]
        if id_title[0].isdigit() and len(id_title) == 2:
          problem_id, title = id_title
          link = f'http://acmicpc.net/problem/{problem_id}'
          problems.append({"problem_id": f"BJ_{problem_id}",
                           "link": link,
                           "level": level,
                           "title": title})
  except:
    logging.warning(traceback.format_exc())
  finally:
    driver.quit()
  return problems


def _crawl_LC_problems(limit):
  logging.info(f"_crawl_LC_problems({limit})")
  driver = get_chrome_driver()
  problems = []
  try:
    driver.get(f"https://leetcode.com/problemset/all/")
    select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'select'))))
    select.select_by_visible_text('all')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

    data = driver.find_element_by_class_name("reactable-data").find_elements_by_tag_name("tr")
    for prob in islice(data, limit):
      problem_id, title, level = prob.text.split('\n')
      problems.append({"problem_id": f"LC_{problem_id}",
                       "level": {"Easy": 1, "Medium": 2, "Hard": 3}[level[level.find(' ') + 1:]],
                       "link": prob.find_element_by_css_selector("a").get_attribute('href'),
                       "title": title.strip()})
  except Exception as e:
    logging.error(traceback.format_exc())
  finally:
    driver.quit()
  return problems


def _crawl_KT_problems_page(page):
  logging.info(f"_crawl_KT_problems_page({page})")
  driver = get_chrome_driver()
  problems = []
  try:
    driver.get(f"https://open.kattis.com/problems?page={page}")
    for l in driver.find_elements_by_css_selector("tr.odd,tr.even"):
      try:
        title, _, _, _, _, _, _, _, level = l.text.rsplit(maxsplit=8)
        link = l.find_element_by_css_selector("a").get_attribute('href')
        problems.append({"problem_id": f"KT_{link.rsplit('/')[-1]}",
                         "title": title,
                         "link": link,
                         "level": level})
      except:
        logging.warning(traceback.format_exc())
  except Exception as e:
    logging.error(traceback.format_exc())
  finally:
    driver.quit()
  return problems


def _crawl_HR_problem(problem_id):
  logging.info(f"_crawl_HR_problem({problem_id})")
  driver = get_chrome_driver()
  try:
    link = f"https://www.hackerrank.com/challenges/{problem_id[3:]}/problem"
    logging.info(link)
    driver.get(link)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'difficulty-block')))
    level = driver.find_elements_by_class_name("difficulty-block")[1].text.split()[-1]
    return {"problem_id": problem_id,
            "link": link,
            "title": driver.find_element_by_class_name("ui-icon-label").text,
            "level": {"Easy": 1, "Medium": 2, "Hard": 3}[level]}
  except:
    logging.warning(traceback.format_exc())


def crawl_problems(site_id, n_thread=None, problem_ids=None):
  """ Return generator of problem DTO """
  logging.debug(f"crawl_problems({site_id}, {n_thread})")
  assert not n_thread or site_id in ["BJ", "KT"], "n_thread only supports in BJ, KT"
  if site_id == "LC":   # no multithread yet TODO
    yield from _crawl_LC_problems()
  elif site_id == "BJ":  # multithread by level
    with ThreadPoolExecutor(n_thread) as ex:
      futures = [ex.submit(_crawl_BJ_problems_level, level) for level in range(31)]
      for future in as_completed(futures):
        yield from future.result()
  elif site_id == "KT":  # multithread by page
    with ThreadPoolExecutor(n_thread) as ex:
      futures = [ex.submit(_crawl_KT_problems_page, page) for page in range(50)]  # TODO, remove hardcode
      for future in as_completed(futures):
        yield from future.result()
  elif site_id == "HR":  # Multithread by question
    with ThreadPoolExecutor(n_thread) as ex:
      futures = [ex.submit(_crawl_HR_problem, problem_id) for problem_id in problem_ids]
      for future in as_completed(futures):
        problem = future.result()
        if problem:
          yield problem
  else:
    raise Exception(f"Site not Supported : {site_id}")


def crawl_solutions(user_site_ids, site_id, n_thread=None):
  logging.info(f"crawl_solutions({user_site_ids}, {site_id})")
  driver = get_chrome_driver()
  if site_id == "BJ":
    with ThreadPoolExecutor(n_thread) as ex:
      future2level = [ex.submit(_crawl_BJ_solutions, BJ_id) for BJ_id in user_site_ids]
      for future in as_completed(future2level):
        yield from future.result()
