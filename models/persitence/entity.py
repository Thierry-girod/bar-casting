from flask_sqlalchemy import SQLAlchemy
from models.persitence import BaseModel


db = SQLAlchemy()
print("11111")
class Entity(BaseModel, db.Model):
    """
        Entity Table
    """

    __tablename__ = 'entity'

    name = db.Column(db.String(60), nullable=False)
    a = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return '<Entity: ID : {} - Name : {}>'.format(self.id, self.name)
