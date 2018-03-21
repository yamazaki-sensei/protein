FROM python:3.6.3

MAINTAINER almichest <almichest.free@gmail.com>

RUN groupadd web
RUN useradd -d /home/server -m bottle

ADD ./temp/server /home/server

RUN pip install -r /home/server/requirements.txt

EXPOSE 8081
ENTRYPOINT [:/usr/local/bin/python", "home/server/src/application/application.py]
USER bottle
