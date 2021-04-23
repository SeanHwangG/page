import subprocess
import logging


def run_command(bash_cmd):
  logging.debug(bash_cmd)
  sp = subprocess.Popen(bash_cmd.split())
  sp.wait()
  return sp.returncode
