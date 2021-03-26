FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /note
WORKDIR /note

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get -y update && \
  apt-get install -y google-chrome-stable vim htop
COPY api/requirements.txt /note/api/requirements.txt
RUN pip install -r /note/api/requirements.txt

COPY . /note
EXPOSE 8080 5432