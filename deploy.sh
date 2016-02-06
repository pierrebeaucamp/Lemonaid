#!/bin/bash
git push heroku master
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku open
