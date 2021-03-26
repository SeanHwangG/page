import concurrent.futures
import unittest
import shutil
import os
import requests
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
from .models.team import Team
from .models.doc import Doc
from .models.member import Member
from .models.problem import Problem
from .models.mock import Mock
from .database import remote_db, local_db
from .common import *
from .app import create_app
from flask import url_for


class PageTester(unittest.TestCase):

  def test_database(self):
    logger.debug("test_database()")
    self.assertIsNotNone(get_oauth_credential())
    self.assertIsNotNone(get_git_credential())
    self.assertIsNotNone(get_service_account_credential())
    self.assertIsNotNone(remote_db)

    print(remote_db.get_all("team"))


if __name__ == '__main__':
  # run single_test
  # suite = unittest.TestSuite()
  # suite.addTest(PageTester("test_new"))
  # runner = unittest.TextTestRunner()
  # runner.run(suite)

  unittest.main()
