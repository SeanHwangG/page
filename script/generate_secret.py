import os


def environment_to_file(name, file_name, type):
  try:
    with open(file_name, "a") as f:
      if type == ".env":
        f.write(f"{name}={os.environ[name]}\n")
      else:
        f.write(f"{os.environ[name]}\n")
  except KeyError as e:
    print(f"Environmnet {name} is not set")
    raise


for env in ["DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DJANGO_LOG_LEVEL"]:
  environment_to_file(env, ".env", ".env")
environment_to_file("SERVICE_ACCOUNT_JSON", "service_account.json", "json")
