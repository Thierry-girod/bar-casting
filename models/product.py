from models.persitence.product import Product, db


def find_by(etablishment_id, *args, order_by='name', **kwargs):
    return Product.find_by(
        *args,
        etablishment_id=etablishment_id,
        order_by=order_by,
        deleted_at=None,
        **kwargs
    )

def search(etablishment_id, name, type, liquid):
    return Product.search(
        etablishment_id=etablishment_id,
        name=name,
        type=type,
        liquid=liquid
    )

def create(*args, **kwargs):
    product = Product(**kwargs)
    product.save()


def delete(id):
    return Product.delete(id)
