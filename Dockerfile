FROM python:3.8

ARG GIT
ARG OAUTH
ARG SERVICE_ACCOUNT
ARG PORT=8080
ARG TEST=false

ENV PORT=${PORT} \
  PYTHONPATH=/page \
  GIT=${GIT} \
  OAUTH=${OAUTH} \
  SERVICE_ACCOUNT=${SERVICE_ACCOUNT}

COPY requirements.txt /
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get -y update && \
  apt-get install -y google-chrome-stable && \
  pip install -r requirements.txt

COPY page/ /page

RUN python -m page.test;
RUN [ "$TEST" = true ] || python -m page.models.member
RUN [ "$TEST" = true ] || python -m page.models.problem
RUN [ "$TEST" = true ] || python -m page.models.doc
RUN [ "$TEST" = true ] || python -m page.models.gist

CMD gunicorn --bind :$PORT --workers 1 --threads 8 "page.app:create_app()";