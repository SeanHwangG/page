from django.db import models
from django.db.models import UniqueConstraint
from util.markdown import extract
import logging


class GitbookManager(models.Manager):
  def parse_summary(self, summary_path):
    logging.debug(f"parse_summary({summary_path})")
    gitbooks = []
    for link in extract(summary_path, "links"):
      logging.info(link["url"])
      directory, file_name = link["url"].rsplit("/", 1)
      gitbooks.append(self.model(directory=directory, file_name=file_name))
    return gitbooks


class HeaderManager(models.Manager):
  def parse_gitbook(self, doc_path, gitbook_id):
    logging.debug(f"parse_gitbook({doc_path}, {gitbook_id})")
    headers = []

    for header in extract(doc_path, "headers"):
      headers.append(self.model(gitbook_id=gitbook_id, level=header["level"], name=header["name"]))
    logging.debug(f"parse_gitbook({doc_path}, {gitbook_id})")

    return headers


class Gitbook(models.Model):
  gitbook_id = models.CharField(max_length=255, null=False, primary_key=True)
  directory = models.CharField(max_length=255, null=False)
  file_name = models.CharField(max_length=255, null=False)
  objects = GitbookManager()

  def __str__(self):
    return f"{self.gitbook_id}"

  def save(self, *args, **kw):
    self.gitbook_id = f'{self.directory}/{self.file_name}'
    super(Gitbook, self).save(*args, **kw)


class Header(models.Model):
  header_id = models.CharField(max_length=255, null=False, primary_key=True)
  gitbook = models.ForeignKey(Gitbook, null=False, on_delete=models.PROTECT)
  name = models.CharField(max_length=255, null=False)
  level = models.IntegerField(default=-1)
  objects = HeaderManager()

  def __str__(self):
    return f"{self.header_id}"

  def save(self, *args, **kw):
    self.header_id = f'{self.gitbook_id}#{self.name}'
    super(Header, self).save(*args, **kw)
