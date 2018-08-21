import enum
from models.persitence import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StockEntryProduct(BaseModel, db.Model):
    """
        Etablishment Table
    """
    __tablename__ = 'stock_entry_product'

    quantity = db.Column(db.Integer(), nullable=False)
    amount_ht = db.Column(db.Float(), nullable=False)
    amount_ttc = db.Column(db.Float(), nullable=False)

    # Foreing key to Entity table
    stock_entry_id = db.Column(db.Integer, db.ForeignKey('stock_entry.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


    def __repr__(self):
        return '<Stock Entry Product: ID: {} - ID Stock: {} - Name : {}>'.format(
            self.id,
            self.stock_entry_id,
            self.name
        )
