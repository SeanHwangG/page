from threading import Lock
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
from threading import Lock
from line_profiler import LineProfiler
from pathlib import Path
import os
import json
import logging
import logging.config

lock = Lock()


class PATH:
  SRC = Path(__file__).resolve().parent
  DB = SRC / 'local_db'
  API = SRC / 'api'
  CRED = SRC / 'cred'
  TEST = SRC / 'test'
  ENV = SRC / '..' / '.env'
  PROBLEM = SRC / '..' / 'book' / 'cs' / 'embed'
  GITHUB = "https://github.com/SeanHwangG/class/tree/main/"


categories = os.listdir(PATH.PROBLEM)


def get_logger(name, level):  # WARNING 30, INFO 20, DEBUG 10
  logging.basicConfig(level=level, format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
  logging.config.dictConfig({'version': 1, 'disable_existing_loggers': True})  # ignore warning from other module
  logger = logging.getLogger(name)

  for hdlr in logger.handlers[:]:  # remove exsiting handlers -> prevents logging twice
    logger.removeHandler(hdlr)

  return logger


def get_service_account_credential():
  if "SERVICE_ACCOUNT" not in os.environ:
    return
  with open(f"{PATH.CRED}/service_account.json", "r") as f:
    service_cred = json.load(f)
  service_cred["private_key"] = os.environ["SERVICE_ACCOUNT"].replace("\\n", "\n")
  return service_cred


def get_git_credential():
  if "GIT" not in os.environ:
    return
  with open(f"{PATH.CRED}/git.json", "r") as f:
    git_cred = json.load(f)
  git_cred["Authorization"] = os.environ['GIT']
  return git_cred


def get_oauth_credential():
  if "OAUTH" not in os.environ:
    return
  with open(f"{PATH.CRED}/oauth.json", "r") as f:
    oauth_cred = json.load(f)
  oauth_cred["client_secret"] = os.environ["OAUTH"]
  return oauth_cred


def get_chrome_driver():
  global lock
  with lock:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver


def html2text(html):
  soup = BeautifulSoup(html, features="html.parser")
  for script in soup(["script", "style"]):
    script.extract()
  text = soup.get_text()
  lines = (line.strip() for line in text.splitlines())
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  return ' '.join(chunk for chunk in chunks if chunk)


load_dotenv(dotenv_path=PATH.ENV)
oauth_credential = get_oauth_credential()
service_account_credential = get_service_account_credential()
git_credential = get_git_credential()
logger = get_logger(__name__, 10 if os.environ.get("DEBUG") != "" else 30)
driver = get_chrome_driver()
