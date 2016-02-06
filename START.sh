#!/bin/bash
heroku local:run python manage.py makemigrations
heroku local:run python manage.py migrate
heroku local
