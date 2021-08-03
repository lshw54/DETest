from flask_wtf import FlaskForm
from wtforms import SubmitField

class VoteForm(FlaskForm):
    vote = SubmitField('Support')