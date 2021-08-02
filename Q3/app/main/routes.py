from flask import render_template, Blueprint, flash, redirect, url_for
from app.models import Vote
from app.main.forms import VoteForm
from app import db

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index", methods=['POST'])
def home():
    form = VoteForm()
    if form.validate_on_submit():
        vote_btn = Vote()
        db.session.add(vote_btn)
        db.session.commit()
        flash('Thanks for Vote!', 'success')
        return redirect(url_for('main.result'))
    return render_template('index.html', title="Index")


@main.route("/result", methods=['GET'])
def about(candidates):
    result = Vote.query.get_or_404(candidates)
    
    return render_template('result.html', title='Vote Result')
    