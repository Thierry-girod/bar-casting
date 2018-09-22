from flask import Blueprint, render_template, redirect, request, url_for

from module.configuration import get_config
from models import stock
from models import product


service_stock = Blueprint('stock', __name__)
conf = get_config()

@service_stock.route('/stock/', methods=['GET'])
def list():
    # Retrieve list of recipe
    list_of_stock = stock.find_by(etablishment_id=1)
    return render_template('stock/index.html', list_of_stock=list_of_stock)

@service_stock.route('/stock/add', methods=['GET'])
def new():
    # Retrieve list of product
    list_of_product = __retrieve_list_products(1)
    return render_template(
        'stock/edit.html',
        etablishment_id=1,
        list_of_product=list_of_product,
        values={})

@service_stock.route('/stock/save', methods=['POST'])
def save():
    print(request.form)
    print(request.form.getlist('entry[quantity][]'))
    print(request.form.getlist('entry[ht][]'))
    print(request.form.getlist('entry[ttc][]'))
    print(request.form.getlist('entry[product_id][]'))

    entry = []
    for key, quantity in enumerate(request.form.getlist('entry[quantity][]')):
        entry.append({
            'quantity': quantity,
            'amount_ht': request.form.getlist('entry[ht][]')[key],
            'amount_ttc': request.form.getlist('entry[ttc][]')[key],
            'product_id': request.form.getlist('entry[product_id][]')[key],
        })
    stock.create(
        etablishment_id=1,
        provider=request.form.get('provider'),
        amount_ttc=request.form.get('amount_ttc'),
        amount_ht=request.form.get('amount_ht'),
        products_entry=entry
    )

    return redirect(url_for('stock.list'))

def __retrieve_list_products(etablishment_id):
    return product.find_by(etablishment_id=etablishment_id)
