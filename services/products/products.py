from flask import Blueprint, render_template, redirect, request, url_for

from module.configuration import get_config
from models import product
from models.persitence.product import ProductType


service_products = Blueprint('products', __name__)
conf = get_config()

@service_products.route('/products/', methods=['GET'])
def list_products():
    # Retrieve list of product
    list_of_product = product.find_by(etablishment_id=1)
    return render_template(
        'products/index.html',
        list_of_product=list_of_product,
        type_1=ProductType.type_1,
        type_2=ProductType.type_2
        )


@service_products.route('/product/filter/', methods=['GET'])
def search():
    liquid = None
    if request.args.get('liquid') == "solid":
        liquid = False
    elif request.args.get('liquid') == "liquid":
        liquid = True

    # Retrieve list of product depending of query made by the user
    list_of_product = product.search(
        1,
        request.args.get('name'),
        request.args.getlist('type[]'),
        liquid
    )
    print(list_of_product)
    return render_template('products/index.html', list_of_product=list_of_product)


@service_products.route('/products/add', methods=['GET'])
def new_product():
    return render_template('products/edit.html', etablishment_id=1, values={})

@service_products.route('/products/save', methods=['POST'])
def save():
    # check if form is valid
    errors = __check_form_valid()
    # If form contains error, go back to form
    if len(errors) > 0:
        return render_template(
            'products/edit.html',
            etablishment_id=1,
            values=request.form,
            field_errors=errors
        )

    # Create product if no error
    product.create(
        etablishment_id=1,
        name=request.form.get('name'),
        type=request.form.get('type'),
        volume=request.form.get('volume'),
        liquid=True if request.form.get('liquid') == "1" else False
    )

    # Redirect to the list of product
    return redirect(url_for('products.list_products'))


@service_products.route('/products/delete/<int:id>', methods=['GET'])
def delete(id):
    # Check if product id belongs to etablishment
    prod = product.find_by(etablishment_id=1, id=id)

    if len(prod) == 0:
        return redirect(url_for('products.list_products'))

    # Check if product still supposed to be in stock

    # Retrieve product and soft delete it
    product.delete(id)

    # Redirect to list of product
    return redirect(url_for('products.list_products'))


def __check_form_valid():
    errors = set()
    if not request.form.get('name', False) or request.form.get('name') == '':
        errors.add('name')
    if not request.form.get('liquid', False):
        errors.add('liquid')
    if not request.form.get('type', False):
        errors.add('type')
    if request.form.get('liquid') == "1" and not request.form.get('volume', '').isdigit():
        errors.add('volume')

    # Return all errors
    return errors
