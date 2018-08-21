import enum
from models.persitence import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
