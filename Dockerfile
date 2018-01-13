FROM python:2.7

MAINTAINER "Hacking Science <https://github.com/hacking-science/>"
LABEL maintainer = "Hacking Science <https://github.com/hacking-science/>"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
