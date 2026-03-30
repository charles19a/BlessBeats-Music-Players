#!/bin/bash
python manage.py migrate
python sync_cloudinary.py
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p $PORT myproject.asgi:application
