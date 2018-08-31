from models.persitence import BaseModel, db

class Entity(BaseModel, db.Model):
    """
        Entity Table
    """

    __tablename__ = 'entity'

    name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Entity: ID : {} - Name : {}>'.format(self.id, self.name)
