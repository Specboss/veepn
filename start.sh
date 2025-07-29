#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py collectstatic --noinput
python -m gunicorn --workers 6 --timeout 200 --bind 0.0.0.0:5000 -k drf_api.workers.NoLifespanUvicornWorker config.asgi:application --reload
