
FROM ubuntu:16.04
FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

ENV  PYTHONUNBUFFERED 1

COPY  ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir /app

WORKDIR /app

COPY ./app app

RUN adduser -D user


RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

COPY base.py base.py

CMD ["python", "base.py"]

USER user

