from flask import Blueprint, render_template

from module.configuration import get_config


service_ingredients = Blueprint('ingredients', __name__)
conf = get_config()

@service_ingredients.route('/ingredients/')
def index():
    return render_template('ingredients/index.html')
