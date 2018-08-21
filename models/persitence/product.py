import enum
from models.persitence import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductType(enum.Enum):
    type_1 = "1"
    type_2 = "2"


class Product(BaseModel):
    """
        Product Table
    """
    __tablename__ = 'product'


    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Enum(ProductType))
    liquid = db.Column(db.Boolean(), default=True)
    quantity = db.Column(db.Integer())

    # Foreing key to Entity table
    etablishment_id = db.Column(db.Integer, db.ForeignKey('etablishment.id'), nullable=False)


    def __repr__(self):
        return '<Product: ID : {} - Name : {}>'.format(self.id, self.name)
