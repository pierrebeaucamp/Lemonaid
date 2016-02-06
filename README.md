# Lemonaid

## Setup

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:pierrebeaucamp/Lemonaid.git
$ cd Lemonaid
$ pip install -r requirements.txt
$ createdb lemonaid
$ heroku git:remote -a rocky-journey-37352
$ heroku local:run python manage.py makemigrations
$ heroku local:run python manage.py migrate
```

## Running locally

```sh
$ python manage.py collectstatic
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ git push heroku master
$ heroku open
```
