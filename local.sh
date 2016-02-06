#!/bin/bash
gulp
python manage.py collectstatic
heroku local:run python manage.py makemigrations
heroku local:run python manage.py migrate
heroku local
