FROM python:3.10-slim-buster

ARG build_env=prod

ENV CURRENT_ENVIRONMENT $build_env

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code /code/logs

WORKDIR /code

# Installting project level python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./src /code