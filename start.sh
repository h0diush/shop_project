#!/bin/bash


python3 manage.py migrate
python3 manage.py loaddata data.json
gunicorn config.wsgi:application --bind 0.0.0.0:8000