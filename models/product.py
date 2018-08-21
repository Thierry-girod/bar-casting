from models.persitence.product import Product


def find_by(etablishment_id, *args,  **kwargs):
    return Product.query.filter_by(etablishment_id=etablishment_id, **kwargs).order_by('name')

def create_product(*args, **kwargs):
    print("create product")
