from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db

class Vote(db.Model):
    vote_id = db.Colunm(db.Interger, primary_key=True)
    id = db.Colunm(db.Interger)
    candidates = db.Colunm(db.String(100), nullable=True)
    datetime = db.Colunm(db.DateTime, index=True, default=datetime.now)
    
    def __repr__(self):
        pass