import logging
import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django_extensions.db.models import TimeStampedModel
from classroom.user.models import User
from classroom.util.markdown import extract


class FileManager(models.Manager):
  def parse_summary(self, summary_path):
    logging.debug("parse_summary(%s)", summary_path)
    gitbooks = []
    for link in extract(summary_path, "links"):
      logging.info(link["url"])
      directory, file_name = link["url"].rsplit("/", 1)
      gitbooks.append(self.model(directory=directory, file_name=file_name))
    return gitbooks


class Repository(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  github_id = models.CharField(max_length=255, null=False, default="")
  name = models.CharField(max_length=255, null=False, default="")
  url = models.URLField(null=False)
  path_env = models.CharField(max_length=255, default="CLASSROOM_PATH")
  tag_type_glob = models.CharField(max_length=255, default="")
  tag_glob = models.CharField(max_length=255, default="*")

  def __str__(self):
    return f"{self.url}"


class File(TimeStampedModel):
  uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, null=False)
  repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
  objects = FileManager()

  def __str__(self):
    return f"{self.name}"
