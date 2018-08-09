import datetime

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from module.configuration import get_config
from services.homepage.homepage import service_homepage
# from services.login.login import login_service

db = SQLAlchemy()

def create_app(debug=False):
    app = Flask(__name__)

    app.config.update(get_config())

    # Configure database
    db.init_app(app)

    create_db_schema(app, db)


    # Blueprint
    app.register_blueprint(service_homepage)
    # app.register_blueprint(convo_service)

    CORS(app)

    return app

def create_db_schema(app, db):
    migrate = Migrate(app, db)
    
    from models.persitence import entity, etablishment, product, user
    from models.persitence import stock_entry, stock_entry_product
