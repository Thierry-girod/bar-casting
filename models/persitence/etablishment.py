from models.persitence import BaseModel, db

class Etablishment(BaseModel, db.Model):
    """
        Etablishment Table
    """
    __tablename__ = 'etablishment'

    name = db.Column(db.String(60), nullable=False)

    # Foreing key to Entity table
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)


    def __repr__(self):
        return '<Etablishment: ID : {} - Name : {}>'.format(self.id, self.name)
