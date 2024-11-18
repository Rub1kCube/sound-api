#! /bin/bash

python /src/manage.py migrate --noinput;
gunicorn -c gunicorn.conf.py sound.asgi:application