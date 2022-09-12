FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


WORKDIR /pet_store/src

COPY . /pet_store/

RUN python -m pip install pipenv==2021.5.29
COPY Pipfile Pipfile.lock /pet_store/
RUN pipenv  install --system --dev

EXPOSE 8000
