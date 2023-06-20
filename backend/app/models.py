from app import db
from datetime import datetime
import sqlalchemy as sa

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    sender = sa.Column(sa.Text())



