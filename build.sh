#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py ensure_site
# En una base nueva (Postgres recién creado) carga el temario; si ya hay
# contenido no hace nada.
python manage.py seed_if_empty
