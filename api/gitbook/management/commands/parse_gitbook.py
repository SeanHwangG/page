from django.core.management.base import BaseCommand, CommandError
from gitbook.models import GitBook, Header
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
      BOOK_PATH = f"{options['gitbook_conf_dir']}/{gitbook_yaml['root']}"
    summary_path = f"{BOOK_PATH}/{gitbook_yaml['structure']['summary']}"
    logging.debug(f"summary_path : {summary_path}")
    for gitbook in GitBook.objects.parse_summary(summary_path):
      gitbook.save()
      for header in Header.objects.parse_markdown(f"{BOOK_PATH}/{gitbook.gitbook_id}", gitbook):
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
