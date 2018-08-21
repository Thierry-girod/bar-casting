import enum
from models.persitence import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
