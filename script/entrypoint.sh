set -e  # exit when error

TEST=${1}
# curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
python3 script/generate_secret.py
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy -credential_file service_account.json
./cloud_sql_proxy -instances=seansdevnote:asia-northeast3:note:5432 &

cd api
if [[ TEST ]]; then
  pylint --rcfile ../setup.cfg *.py
  python manage.py test
else
  python manage.py collectstatic --noinput
  python manage.py migrate
  python manage.py runserver
fi
