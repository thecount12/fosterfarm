# Canna Foster Farm Management  

Farm Management Software

### setup environment

1. virtualenv -p /usr/local/bin/python3.7 ~/.fosterenv
2. source ~/.fosterenv/bin/activate
3. pip install -r requirements

### First Steps

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

Fix problems if any...

python manage runserver
