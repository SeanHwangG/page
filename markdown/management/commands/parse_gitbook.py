from django.core.management.base import BaseCommand, CommandError
from markdown.models import Markdown, Header
from django.conf import settings
import io
import logging
import yaml
import panflute


class Command(BaseCommand):
  help = 'Closes the specified poll for voting'

  def add_arguments(self, parser):
    parser.add_argument('-g', '--gitbook_conf_dir', type=str, help="directory path where .gitbook.yaml is", default=f"{settings.NOTE_DIR}")

  def handle(self, *args, **options):
    with open(f"{options['gitbook_conf_dir']}/.gitbook.yaml", 'r') as stream:
      gitbook_yaml = yaml.safe_load(stream)
      book_path = f"{options['gitbook_conf_dir']}/{gitbook_yaml['root']}"
    summary_path = f"{book_path}/{gitbook_yaml['structure']['summary']}"
    logging.debug(f"book_path : {book_path}")
    logging.debug(f"summary_path : {summary_path}")
    for markdown in Markdown.objects.parse_summary(summary_path):
      if markdown.markdown_id == "":
        pass  # FIXME
      markdown.save()
      for header in Header.objects.parse_markdown(f"{book_path}/{markdown.markdown_id}", markdown):
        header.save()
    """
    for poll_id in options['poll_id']:
      try:
        poll = Poll.objects.get(pk=poll_id)
      except Poll.DoesNotExist:
        raise CommandError('Poll "%s" does not exist' % poll_id)

      poll.opened = False
      poll.save()

      self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
    """
