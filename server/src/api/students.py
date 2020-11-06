import sys
import time
import multiprocessing as mp
import re
import fire
import json
import re
import pathlib
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PAGE_PATH = '/Users/sean/github/page/server/src'
CHAPTERS = ["", "[1] Print", "[2] Input", "[3] Conditional", "[4] Loop | Iterables", "[5] Hashing", "[6] Sort", "[7] Tricks", "[8] Advanced Data structure", "", "[10] Math", "[11] Greedy", "[12] DP", "[13] Recursion | Backtrack", "[14] Graph", "[16] concurrency"]

def get_students(*, to_html=None, name=None):
    print(to_html, name)
    with open(f"{PAGE_PATH}/data/students.json", 'r') as f:
        students = json.load(f)
    if name:
        students = list(filter(lambda student: student['name'] == name, students))

    if to_html:
        with open(f"{PAGE_PATH}/data/problems.json", 'r') as f:
            problems = json.load(f)
        html = ""
        for student in students:
            html += student['name']
            cur_chapter, cur_ul = "", ""
            for prob_title in student['todo']:
                problem = next(filter(lambda prob: prob['id'] == prob_title, problems), "")
                try:
                    if cur_chapter != problem["chapter"]:
                            cur_chapter = problem["chapter"]
                            html += CHAPTERS[int(cur_chapter)] + "<br>"
                except:
                    pass
                try:
                    if cur_ul != problem["ul"]:
                        cur_ul = problem["ul"]
                        html += cur_ul + "<br>"
                except:
                    pass
                html += problem['link'] + "<br>"
        return html

    return students

def update_student(student):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)

    try:
        driver.get(f"https://www.acmicpc.net/user/{student['id']}")
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
        student['solved'] = driver.find_element_by_class_name('panel-body').text.split()
    except Exception:
        driver.quit()
    else:
        driver.quit()
    return student

def update_students():
    with open(f"{PAGE_PATH}/data/students.json", 'r') as f:
        students = json.load(f)

    with open(f"{PAGE_PATH}/data/problems.json", 'r') as f:
        problems = json.load(f)

    with mp.Pool(16) as pool:
        students = pool.map(update_student, students)

    for student in students:
        todos = [problem for problem in problems if problem['id'] not in student['solved'] and problem['chapter'] != -1]
        todos.sort(key=lambda problem: (problem['chapter'], problem.get("ul", ""), problem['level']))
        student['todo'] = [problem["id"] for problem in todos]
        if 'id' not in student:
            student['id'] = ""

    with open(f"{PAGE_PATH}/data/students.json", 'w') as f:
        json.dump(students, f, ensure_ascii=False)


if __name__ == "__main__":
    fire.Fire()