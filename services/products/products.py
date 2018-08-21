from flask import Blueprint, render_template, redirect, request

from module.configuration import get_config
from models import product


service_products = Blueprint('products', __name__)
conf = get_config()

@service_products.route('/products/', methods=['GET'])
def list_products():
    return render_template('products/index.html')


@service_products.route('/products/add', methods=['GET'])
def new_product():
    return render_template('products/edit.html', etablishment_id=1)

@service_products.route('/products/save', methods=['POST'])
def save():
    # check if form is valid
    errors = __check_form_valid()
    # If form contains error, go back to form
    if len(errors) > 0:
        return render_template(
            'products/edit.html',
            etablishment_id=1,
            values=request.form
        )
    product.create_product(
        etablishment_id=1,
        name=request.form.get('name'),
        type=request.form.get('type'),
        volume=request.form.get('volume')
    )
    print(request.form.get('name'))
    print(request.form.get('liquid'))
    print(request.form.get('type'))
    print(request.form.get('volume'))
    return render_template('products/edit.html', etablishment_id=1)


@service_products.route('/products/delete/<int:id>', methods=['GET'])
def delete_product(id):
    # Check if product id belongs to etablishment

    # Check if product still supposed to be in stock

    # Retrieve product and soft delete it

    # Redirect to list of product
    return redirect(url_for('products.list_products'))


def __check_form_valid():
    errors = set()
    if not request.form.get('name', False):
        errors.add('name')
    if not request.form.get('liquid', False):
        errors.add('liquid')
    if not request.form.get('type', False):
        errors.add('type')
    if request.form.get('liquid') == "1" and not is_numeric(request.form.get('volume')):
        errors.add('volume')
    return errors
