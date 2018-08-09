DEV :
- Run server :
1. source venv/bin/activate
2. gunicorn --bind 0.0.0.0:8000 --reload wsgi-core --log-level=DEBUG


- Database Migration
1. source venv/bin/activate
2. First time : flask db init
3. flask db migrate
4. flask db upgrade
