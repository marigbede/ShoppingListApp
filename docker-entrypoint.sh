#!/bin/sh

python manage.py migrate && python manage.py test && python manage.py runserver 0.0.0.0:$PORT