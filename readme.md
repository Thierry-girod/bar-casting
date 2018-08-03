DEV :
- Run server :
gunicorn --bind 0.0.0.0:8000 --reload wsgi-core --log-level=DEBUG
