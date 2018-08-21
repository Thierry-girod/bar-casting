import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel():
    """
        Base classe should be extended by all models
    """

    # __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime)
