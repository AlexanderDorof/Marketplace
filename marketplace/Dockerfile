FROM python:3.9-alpine

WORKDIR /usr/src/marketplace

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/marketplace/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/marketplace/
RUN python3 manage.py migrate

