from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db

class Vote(db.Model):
    vote_id = db.Column(db.Integer, primary_key=True)
    candidates = db.Column(db.Text, nullable=True)
    datetime = db.Column(db.DateTime, index=True, default=datetime.now)
    
    def __repr__(self):
        return f"Vote('{self.candidates}','{self.datetime}', '{self.vote_id}')"