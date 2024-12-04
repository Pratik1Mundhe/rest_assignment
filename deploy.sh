#!/bin/bash
npm install apidoc
pip install virtualenv
virtualenv _venv
source _venv/bin/activate
pip install -r requirements_lambda.txt
DJANGO_SETTINGS_MODULE=rest_assignment.settings."$1" python manage.py build -adj
DJANGO_SETTINGS_MODULE=rest_assignment.settings."$1" python manage.py mocktests
DJANGO_SETTINGS_MODULE=rest_assignment.settings."$1" python manage.py s3push -d --bucket swagger-apidocs --prefix rest_assignment/"$1"
zappa update alpha
zappa manage "migrate --no-input"
