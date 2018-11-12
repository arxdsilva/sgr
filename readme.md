# Requirements

- Python 3
- Django 2.1.3
- SQLite 3

# Obs

This is my very first Django app and I've never fooled around with python for very long, so enjoy!

# Setup

## Clone project
```
    $ git clone git@github.com:arxdsilva/sgr.git
```

## Create user
```
    $ python manage.py createsuperuser
```

## Run migrations
```
    $ python manage.py migrate
```

## Test
```
    $ ./manage.py test
```

## Run the app
```
    $ python manage.py runserver
```
Go to `http://127.0.0.1:8000/` and It's alive!

## Login
Go to `http://127.0.0.1:8000/admin` and login with your credentials recently created.
