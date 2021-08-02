from flask_wtf import FlaskForm
from wtforms import SubmitField

class VoteForm(FlaskForm):
    vote = SubmitField('Post', render_kw={"class": "btn btn-success", "id": "btn-sub"})