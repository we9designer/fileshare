FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /fileshare/requirements.txt
RUN pip install -r /fileshare/requirements.txt

COPY . /fileshare/
WORKDIR /fileshare/

EXPOSE 8000