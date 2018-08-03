from flask import Blueprint, render_template

from module.configuration import get_config


service_homepage = Blueprint('homepage', __name__)
conf = get_config()

@service_homepage.route('/')
def index():
    return render_template('homepage/homepage.html')
