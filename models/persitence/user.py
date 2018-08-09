from models.persitence import BaseModel
from services.app import db

class User(BaseModel, db.Model):
    """
        Etablishment Table
    """
    __tablename__ = 'user'

    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(60), nullable=False)


    # Foreing key to Entity table
    etablishment_id = db.Column(db.Integer, db.ForeignKey('etablishment.id'), nullable=False)


    def __repr__(self):
        return '<Etablishment: ID : {} - Name : {}>'.format(self.id, self.name)
