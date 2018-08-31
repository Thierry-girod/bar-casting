import enum
from models.persitence import BaseModel, db
from models.persitence.product import Product
from models.persitence.recipe_product import RecipeProduct

class Recipe(BaseModel, db.Model):
    """
        Product Table
    """
    __tablename__ = 'recipe'

    name = db.Column(db.String(120), nullable=False)

    # Foreing key to Entity table
    etablishment_id = db.Column(db.Integer, db.ForeignKey('etablishment.id'), nullable=False)

    def __repr__(self):
        return '<Recipe: ID : {} - Name : {}>'.format(self.id, self.name)

    @classmethod
    def find_by(cls, *args, order_by='name', **kwargs):
        return cls.query.filter_by(deleted_at=None, **kwargs).order_by(order_by).all()

    @classmethod
    def list_recipe_with_volume_and_nb_product(cls, etablishment_id, order_by):
        return db.session.query(
            Recipe.id.label('id'),
            Recipe.name.label('name'),
            db.func.sum(RecipeProduct.quantity).label('quantity'),
            db.func.count(RecipeProduct.product_id).label('nb_product')
        ).filter_by(
            etablishment_id=etablishment_id,
            deleted_at=None
        ).join(
            RecipeProduct, RecipeProduct.recipe_id == Recipe.id
        ).group_by(
            Recipe.id
        ).order_by(
            Recipe.name
        ).all()
