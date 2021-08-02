from flask import render_template, Blueprint, flash, redirect, url_for
from app.models import Vote
from app.main.forms import VoteForm
from app import db
import datetime

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index", methods=['GET', 'POST'])
def home():
    form = VoteForm()
    #if form.validate_on_submit():
    c = '薯片'
    vote_btn = Vote(candidates=c)
    db.session.add(vote_btn)
    db.session.commit()
    Vote.id += 1
    Vote.vote_id += 1
    flash('Thanks for Vote!', 'success')
        #return redirect(url_for('main.result'))
    return render_template('index.html', title="Index", form=form)


@main.route("/result", methods=['GET'])
def result():
    result = Vote.query.order_by(Vote.candidates).all()
    #tables=[df.to_html(classes='data', header="true")]
    print(result)
    return render_template('result.html', title='Vote Result', result=result)
    