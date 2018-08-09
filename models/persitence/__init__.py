import datetime
from services.app import db

class BaseModel():
    """
        Base classe should be extended by all models
    """
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = db.Column(db.DateTime)
