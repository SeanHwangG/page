import sys
import time
import multiprocessing as mp
import re
import fire
import json
import re
import pathlib
import unicodedata
from bs4 import BeautifulSoup
# from .page import update_page
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PAGE_PATH = '/Users/sean/github/page/server/src'

def get_problems(*, original=None, to_html=None, min_level = None, max_level= None, chapter = None, student = None):
    with open(f"{PAGE_PATH}/data/problems.json", 'r') as f:
        problems = json.load(f)
    if chapter:
        problems = list(filter(lambda problem: problem['chapter'] == chapter, problems))
    if min_level:
        problems = list(filter(lambda problem: problem['level'] >= min_level, problems))
    if max_level:
        problems = list(filter(lambda problem: problem['level'] <= max_level, problems))
    if student:
        problems = list(filter(lambda problem: problem not in student['solved'], problems))
    
    if to_html:
        html = ""
        for chapter in range(1, 11):
            html += f"<h1>{chapter}</h1>"
            for problem in filter(lambda problem : problem['chapter'] == chapter, problems):
                html += "<br>"
                html += problem['link']
                html += "<br>"
                if 'python' in problem:
                    html += '<br>'.join(problem["python"])
        return html
    else:
        return problems

def update_problems(*, update_page = None, update_level = None):
    if update_level:
        with mp.Pool(16) as pool:
            levels = pool.map(get_problems_level, range(1, 31))
        problems = [problem for level in levels for problem in level]
    else:
        with open(f"{PAGE_PATH}/data/problems.json", 'r') as f:
            problems = json.load(f)

    if update_page:
        bs = BeautifulSoup(open(f"{PAGE_PATH}/data/teaching_teacher.html", 'r'), "html.parser")
        i = 0
        cur_h2, cur_h3, cur_ul = None, None, None
        tags = list(bs.find("h1", text="Algorithm").next_siblings)
        while i < len(tags):
            tag = tags[i]
            prob_match = re.search(r'(BJE?)_(\d+) (.*) \((.*)\)', tag.text)
            if tag.name == "h2":
                cur_h2 = tag.text
            elif tag.name == "h3":
                cur_h3 = tag.text
            elif tag.name == "ul":
                cur_ul = tag.text
            elif tag.name == "p" and prob_match:
                pid = prob_match.group(2)
                try:
                    cur_problem = next(filter(lambda problem: problem['id'] == pid, problems))
                except:
                    i += 1
                    continue
                p = ""
                while tags[i + 1].name == "p" and not re.search(r'(BJE?)_(\d+) (.*) \((.*)\)', tag.text):
                    i += 1
                    p += tags[i].text + "\n"
                try:
                    del cur_problem['python']
                except:
                    pass
                cur_problem['type'] = prob_match.group(1)
                cur_problem['title'] = prob_match.group(3)
                cur_problem['link'] = f'<a href="http://acmicpc.net/problem/{pid}">{prob_match.group(3)} ({cur_problem["level"]})</a>'
                cur_problem['p'] = p
                cur_problem['h2'] = cur_h2
                cur_problem['h3'] = cur_h3
                cur_problem['ul'] = cur_ul
            i += 1

    with open(f"{PAGE_PATH}/data/problems.json", 'w') as f:
        json.dump(problems, f, ensure_ascii=False)

def get_problems_level(level):
    problems = []
    chrome_options = Options()
    chrome_options.add_argument('headless')  
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    try:
        level_problems = []
        for page in range(1, 100):
            driver.get(f"https://solved.ac/problems/level/{level}?sort=id&direction=asc&page={page}")
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
            lines = driver.find_element_by_class_name('contents').text
            if '해당하는 문제가 없습니다' in lines:
                break
            for line in lines.split('\n'):
                level_problems.extend(re.findall(r'^ (\d+)', line))
        for problem in level_problems:
            problems.append({'id' : problem, 'level' : level})
    except Exception:
        driver.quit()
    else:
        driver.quit()
    return problems


if __name__ == "__main__":
    update_problems(update_page= True)
    # fire.Fire()