#!/bin/bash

# Faire un pull
git pull

# Mettre à jour les migrations
python3 src/manage.py makemigrations

# Faire Migrer
python3 src/manage.py migrate

# Collecter les fichiers static
python3 src/manage.py collectstatic

# Redemarrer gunicorn
sudo systemctl restart gunicorn