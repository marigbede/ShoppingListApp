FROM python:3.7-buster

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PORT 8000

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./manage.py /opt/app/manage.py
COPY ./docker-entrypoint.sh /opt/app/docker-entrypoint.sh
COPY ShoppingListApp /opt/app/ShoppingListApp

RUN chmod +x /opt/app/docker-entrypoint.sh

ENTRYPOINT [ "sh", "docker-entrypoint.sh" ]