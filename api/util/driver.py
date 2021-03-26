from threading import Lock
from django.conf import settings
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_chrome_driver():
  with Lock():
    chrome_options = Options()
    if not settings.DEBUG:
      chrome_options.add_argument('--headless')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver
