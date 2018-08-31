from flask import Blueprint, render_template, redirect, request, url_for

from module.configuration import get_config
from models import recipe
from models import product


service_recipe = Blueprint('recipe', __name__)
conf = get_config()

@service_recipe.route('/recipe/', methods=['GET'])
def list():
    # Retrieve list of recipe
    list_of_recipe = recipe.list_recipe_with_volume_and_nb_product(1)
    return render_template('recipe/index.html', list_of_recipe=list_of_recipe)

@service_recipe.route('/recipe/filter/', methods=['GET'])
def search():
    # Retrieve list of recipe
    list_of_recipe = recipe.search(1, request.args.get('name', ''))
    return render_template('recipe/index.html', list_of_recipe=list_of_recipe)

@service_recipe.route('/recipe/add', methods=['GET'])
def new():
    # Retrieve list of product
    list_of_product = __retrieve_list_products(1)
    return render_template(
        'recipe/edit.html',
        etablishment_id=1,
        list_of_product=list_of_product,
        values={})


@service_recipe.route('/recipe/save', methods=['POST'])
def save():
    # print(request.form.get('recipe').get('quantity'))
    # check if form is valid
    errors = __check_form_valid()
    print(errors)
    # return None
    # If form contains error, go back to form
    if len(errors) > 0:
        list_of_product = __retrieve_list_products(1)
        return render_template(
            'recipe/edit.html',
            etablishment_id=1,
            values=request.form,
            list_of_product=list_of_product,
            field_errors=errors
        )

    # Create dict containing product_id and quantity
    product_quantity = {}
    for key, product_id in enumerate(request.form.getlist('product_id[]')):
        quantity = request.form.getlist('quantity[]')[key]
        # product_id = request.form.getlist('product_id[]').get(key)
        product_quantity[product_id] = quantity

    # Create recipe if no error
    obj_recipe = recipe.create(
        etablishment_id=1,
        name=request.form.get('name'),
        product_quantity=product_quantity
    )

    # Redirect to the list of product
    return redirect(url_for('recipe.list'))


@service_recipe.route('/recipe/delete/<int:id>', methods=['GET'])
def delete(id):
    print(id)
    # Check if product id belongs to etablishment
    rec = recipe.find_by(etablishment_id=1, id=id)

    if len(rec) == 0:
        return redirect(url_for('recipe.list'))

    # Check if product still supposed to be in stock

    # Retrieve product and soft delete it
    recipe.delete(id)

    # Redirect to list of product
    return redirect(url_for('recipe.list'))


def __retrieve_list_products(etablishment_id):
    return product.find_by(etablishment_id=etablishment_id)

def __check_form_valid():
    errors = set()
    if not request.form.get('name', False) or request.form.get('name') == '':
        errors.add('name')
    list_product_id = request.form.getlist('product_id[]')
    nb_product = 0
    for product_id in list_product_id:
        if not product_id.isdigit():
            errors.add('product_id')
        else:
            nb_product += 1
    nb_quantity = 0
    list_quantity = request.form.getlist('quantity[]')
    for quantity in list_quantity:
        if not quantity.isdigit():
            errors.add('quantity')
        else:
            nb_quantity += 1
    if nb_product != nb_quantity:
        errors.add('product_quantity')

    # Return all errors
    return errors
