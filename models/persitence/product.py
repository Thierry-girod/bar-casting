import enum
from models.persitence import BaseModel, db

class ProductType(enum.Enum):
    type_1 = "1"
    type_2 = "2"


class Product(BaseModel, db.Model):
    """
        Product Table
    """
    __tablename__ = 'product'


    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Enum(ProductType))
    liquid = db.Column(db.Boolean(), default=True)
    volume = db.Column(db.Integer())

    # Foreing key to Entity table
    etablishment_id = db.Column(db.Integer, db.ForeignKey('etablishment.id'), nullable=False)


    def __repr__(self):
        return '<Product: ID : {} - Name : {}>'.format(self.id, self.name)

    @classmethod
    def find_by(cls, *args, order_by='name', **kwargs):
        return Product.query.filter_by(**kwargs).order_by(order_by).all()

    @classmethod
    def search(cls, *args, etablishment_id, name='', type=[ProductType.type_1, ProductType.type_2], liquid=None):
        if len(type) == 0:
            type=[ProductType.type_1, ProductType.type_2]
        q_set = db.session.query(
            Product
        ).filter(
            cls.etablishment_id==etablishment_id,
            cls.name.like('%{}%'.format(name)),
            cls.type.in_((type)),
            # cls.liquid==liquid if liquid != None else cls.liquid == True or cls.liquid = False,
            cls.deleted_at==None
        ).order_by('name')
        return q_set.all()
