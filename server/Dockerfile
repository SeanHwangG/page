
FROM python:3.7
RUN pip install Flask gunicorn requests pyrebase oauthlib selenium google-api-python-client google-auth-oauthlib flask_login fire beautifulsoup4
#COPY requirements.txt /tmp/
# RUN pip install --requirement /tmp/requirements.txt

COPY src/ /app
WORKDIR /app
ENV PORT 8080


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app