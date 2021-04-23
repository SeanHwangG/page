from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
  help = 'Crawl Solution'

  def add_arguments(self, parser):
    parser.add_argument('-t', '--tag_dir', type=str, help="Glob path for each tag", default="")
    parser.add_argument('-p', '--problem_path', type=str, help="Glob path for solutions relative to tag_dir")
    parser.add_argument('-u', '--user_name', type=str, help="user_name")

  def handle(self, *args, tag_dir: str, problem_path: str, user_name: str, **options):
    logging.info(f"handle({tag_dir}, {problem_path}, {user_name})")
    site_ids = set(site.site_id for site in Site.objects.all())
    new_tag = new_solution = 0
    for file in Path(".").glob(problem_dir):
      logging.debug(file)
      tag_id, title = str(file).rsplit("/", 2)[1:]
      tag, created = Tag.objects.get_or_create(tag_id=tag_id)
      if title[:2] not in site_ids:
        pass
      if created:
        new_tag += 1
        logging.info(f"Created : tag {tag}")

      site_code, problem_code = title[:-3].split("_", 1)
      site = site.objects.get(code=site_code)
      try:
        problem = Problem.objects.get(site=site, code=problem_code)
      except Exception as e:
        logging.warn(traceback.format_exc())
        continue
      problem.tags.set(Tag.objects.filter(tag_id=tag_id))
      url_path = str(file.resolve()).split('interview/', 1)[1]
      solution, created = Solution.objects.update_or_create(user=user, problem=problem, defaults={
                                                            "link": f"{settings.PROBLEM_GITHUB}/tree/main/{url_path}"})
      if created:
        new_solution += 1
        logging.info(f"Created : solution {solution}")
    logging.info(f"Created : {new_tag} tags from directory")
    logging.info(f"Created : {new_solution} solutions from directory")
