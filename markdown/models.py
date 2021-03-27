from django.db import models
from django.db.models import UniqueConstraint
from util.markdown import extract
import logging


class MarkdownManager(models.Manager):
  def parse_summary(self, summary_path):
    logging.debug(f"parse_summary({summary_path})")
    markdowns = []
    for link in extract(summary_path, "links"):
      logging.info(link["url"])
      directory, file_name = link["url"].rsplit("/", 1)
      markdowns.append(self.model(directory=directory, file_name=file_name))
    return markdowns


class HeaderManager(models.Manager):
  def parse_markdown(self, doc_path, markdown_id):
    logging.debug(f"parse_markdown({doc_path}, {markdown_id})")
    headers = []

    for header in extract(doc_path, "headers"):
      headers.append(self.model(markdown_id=markdown_id, level=header["level"], name=header["name"]))
    logging.debug(f"parse_markdown({doc_path}, {markdown_id})")

    return headers


class Markdown(models.Model):
  markdown_id = models.CharField(max_length=255, null=False, primary_key=True)
  directory = models.CharField(max_length=255, null=False)
  file_name = models.CharField(max_length=255, null=False)
  objects = MarkdownManager()

  def __str__(self):
    return f"{self.markdown_id}"

  def save(self, *args, **kw):
    self.markdown_id = f'{self.directory}/{self.file_name}'
    super(Markdown, self).save(*args, **kw)


class Header(models.Model):
  header_id = models.CharField(max_length=255, null=False, primary_key=True)
  markdown = models.ForeignKey(Markdown, null=False, on_delete=models.PROTECT)
  name = models.CharField(max_length=255, null=False)
  level = models.IntegerField(default=-1)
  objects = HeaderManager()

  def __str__(self):
    return f"{self.header_id}"

  def save(self, *args, **kw):
    self.header_id = f'{self.markdown_id}#{self.name}'
    super(Header, self).save(*args, **kw)
