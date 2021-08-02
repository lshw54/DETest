from flask_wtf import FlaskForm
from wtforms import SubmitField

class VoteForm(FlaskForm):
    vote1 = SubmitField(label='Support')
    vote2 = SubmitField('Support', render_kw={"class": "btn btn-success", "id": "btn-sub"})
    vote3 = SubmitField('Support', render_kw={"class": "btn btn-success", "id": "btn-sub"})