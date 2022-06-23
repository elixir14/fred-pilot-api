release: python manage.py migrate && ./manage.py createsuperuser --username admin --noinput || echo "Already exists"
web: gunicorn fred-pilot-api.wsgi:application
