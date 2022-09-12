FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


WORKDIR /pet_store/src

COPY . /pet_store/
COPY requirements.txt /pet_store/src

RUN pip install -r requirements.txt

EXPOSE 8000
