import enum
from models.persitence import BaseModel, db

class RecipeProduct(BaseModel, db.Model):
    """
        Product Table
    """
    __tablename__ = 'recipe_product'

    quantity = db.Column(db.Float(), nullable=False)

    # Foreing key to Recipe table
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return '<Recipe product: ID : {} - Id Recipe : {} - Name : {}>'.format(
            self.id,
            self.id,
            self.name
        )

    @classmethod
    def delete_recipe(cls, recipe_id):
        for recipe_product in db.session.query(RecipeProduct).filter(recipe_id==recipe_id):
            RecipeProduct.delete(recipe_product.id)

    @classmethod
    def find_by(cls, *args, order_by='name', **kwargs):
        return cls.query.filter_by(deleted_at=None, **kwargs).order_by(order_by).all()
