#!/bin/bash
git push --force heroku master
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku open
