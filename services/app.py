import datetime

from flask import Flask
from flask_cors import CORS

from module.configuration import get_config
from services.homepage.homepage import service_homepage
# from services.login.login import login_service


def create_app(debug=False):
    app = Flask(__name__)

    app.register_blueprint(service_homepage)
    # app.register_blueprint(convo_service)

    CORS(app)


    return app
