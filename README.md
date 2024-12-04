# rest_assignment


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
```

## install requirements

```bash
pip install -r requirements_project.txt
pip install -r requirements_test.txt
```

## running django management commands & usage

```sh
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=rest_assignment.settings.local
python manage.py build -a rest_app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```