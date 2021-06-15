#!/bin/sh
# espera a la db
sleep 5
# correr migraciones
python manage.py makemigrations
python manage.py migrate
# poblar la db
python manage.py runscript poblar_db
# inicio el servidor
python manage.py runserver 0.0.0.0:8002