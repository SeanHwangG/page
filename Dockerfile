FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /classroom
WORKDIR /classroom

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get -y update && \
  apt-get install -y google-chrome-stable vim htop
COPY requirements.txt /classroom/requirements.txt
RUN pip install -r /requirements.txt

COPY . /classroom/

EXPOSE 8080 5432