from django.db import models
from django.db.models import UniqueConstraint
from util.markdown import extract
import logging


class GitBookManager(models.Manager):
  def parse_summary(self, summary_path):
    gitbooks = []
    for link in extract(summary_path, "links"):
      directory, file_name = link["url"].rsplit("/", 1)
      gitbooks.append(self.model(directory=directory, file_name=file_name))
    return gitbooks


class HeaderManager(models.Manager):
  def parse_markdown(self, doc_path, gitbook):
    logging.debug(f"parse_markdown({doc_path}, {gitbook})")
    headers = []

    for header in extract(doc_path, "headers"):
      headers.append(self.model(gitbook=gitbook))
    logging.debug(f"parse_markdown({doc_path}, {gitbook})")

    return headers


class GitBook(models.Model):
  gitbook_id = models.CharField(max_length=255, null=False, primary_key=True)
  directory = models.CharField(max_length=255, null=False)
  file_name = models.CharField(max_length=255, null=False)
  objects = GitBookManager()

  def __repr__(self):
    return f"{self.__dict__}"

  def save(self, *args, **kw):
    self.gitbook = f'{self.directory}/{self.file_name}'
    super(GitBook, self).save(*args, **kw)


class Header(models.Model):
  header_id = models.CharField(max_length=255, null=False, primary_key=True)
  gitbook = models.ForeignKey(GitBook, null=False, on_delete=models.PROTECT)
  name = models.CharField(max_length=255, null=False)
  level = models.IntegerField(default=-1)
  objects = HeaderManager()

  def save(self, *args, **kw):
    self.header_id = f'{self.gitbook}#{self.name}'
    super(Header, self).save(*args, **kw)
