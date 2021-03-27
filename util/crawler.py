from threading import Lock
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

import json
import logging
import re
import os
import time


def get_chrome_driver():
  with Lock():
    chrome_options = Options()
    if not settings.DEBUG:
      chrome_options.add_argument('--headless')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver


def _crawl_BJ_solutions(BJ_id):
  logging.info(f"_crawl_BJ_solutions({BJ_id})")
  driver = get_chrome_driver()
  try:
    driver.get(f"https://www.acmicpc.net/user/{BJ_id}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
    yield {"user_id": BJ_id,
           "problem_ids": [f"BJ_{problem}" for problem in driver.find_element_by_class_name('panel-body').text.split()]}
  except Exception as e:
    logging.warning(f"{e}")
  finally:
    driver.quit()


def _crawl_BJ_problems(level):
  logging.debug(f"_crawl_BJ_problems({level})")
  driver = get_chrome_driver()
  problems = []
  try:
    for page in range(1, 100):
      driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
      lines = driver.find_element_by_class_name('contents').text
      if '해당하는 문제가 없습니다' in lines:
        break
      for line in lines.split("\n"):                      # ex)
        line = line.strip("STANDARD").strip()             # 10430 나머지 계산 STANDARD -> 10430 나머지 계산
        id_title = line.split(' ', 1)                     # 10430 나머지 계산 -> [10430, 나머지 계산]
        if id_title[0].isdigit() and len(id_title) == 2:
          problem_id, title = id_title
          link = f'http://acmicpc.net/problem/{problem_id}'
          problems.append({
              "problem_id": f"BJ_{problem_id}",
              "link": link,
              "level": level,
              "title": title
          })
  except Exception as e:
    logging.warn(e)
  finally:
    driver.quit()
  return problems


def _crawl_LC_problems(limit):
  logging.info(f"_crawl_LC_problems({limit})")
  driver = get_chrome_driver()
  problems = []
  try:
    select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'select'))))
    select.select_by_visible_text('all')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

    data = driver.find_element_by_class_name("reactable-data").find_elements_by_tag_name("tr")
    for prob in islice(data, limit):
      problem_id, title, level = prob.text.split('\n')
      problems.append({
          "problem_id": f"LC_{problem_id}",
          "level": {"Easy": 1, "Medium": 2, "Hard": 3}[level[level.find(' ') + 1:]],
          "link": prob.find_element_by_css_selector("a").get_attribute('href'),
          "title": title
      })
  except Exception as e:
    logging.error(e)
  finally:
    driver.quit()
  return problems


def crawl_problems(site_id, limit=None, level=None, n_thread=None):
  logging.debug(f"crawl_problems({site_id}, {limit}, {level}, {n_thread})")
  assert not limit or site_id == "LC", "Limit only supports in LC"
  assert not level or site_id == "BJ", "Level only supports in BJ"
  assert not n_thread or site_id == "BJ", "n_thread only supports in BJ"
  if site_id == "LC":
    yield from _crawl_LC_problems(limit)
  elif site_id == "BJ":
    with ThreadPoolExecutor(10) as ex:
      future2level = [ex.submit(_crawl_BJ_problems, level) for level in ([level] if level else range(31))]
      for future in as_completed(future2level):
        yield from future.result()
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
