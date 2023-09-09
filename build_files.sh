#!/bin/bash

echo "BUILD START"

# Install project dependencies using the specified Python version
python3.11 -m pip install -r requirements.txt

# Collect static files for your Django project
python3.11 manage.py collectstatic --noinput --clear

echo "BUILD END"
