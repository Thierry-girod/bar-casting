from models.persitence.stock_entry import StockEntry, db
from models.persitence.stock_entry_product import StockEntryProduct


def find_by(etablishment_id, *args, order_by='created_at', **kwargs):
    return StockEntry.find_by(
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

def create(*args, products_entry, **kwargs):
    stock = StockEntry(**kwargs)
    stock.save()
    print(stock.id)

    print(products_entry)
    for data in products_entry:
        print(data)
        data['stock_entry_id'] = stock.id
        stock_product = StockEntryProduct(
            **data
        )
        stock_product.save()

    return stock


def delete(id):
    pass
