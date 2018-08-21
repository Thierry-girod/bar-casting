import enum
from models.persitence import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class BillStatus(enum.Enum):
    to_pay = "0"
    payed = "1"
    wont_pay = "2"



class StockEntry(BaseModel, db.Model):
    """
        Etablishment Table
    """
    __tablename__ = 'stock_entry'

    provider = db.Column(db.String(120), nullable=False)
    amount_ht = db.Column(db.Float(), nullable=False)
    amount_ttc = db.Column(db.Float(), nullable=False)
    bill_status = db.Column(db.Enum(BillStatus))
    path_to_bill = db.Column(db.Text(), nullable=True)
    pay_date = db.Column(db.DateTime())

    # Foreing key to Entity table
    etablishment_id = db.Column(db.Integer, db.ForeignKey('etablishment.id'), nullable=False)


    def __repr__(self):
        return '<Stock Entry: ID : {} - Name : {}>'.format(self.id, self.name)
