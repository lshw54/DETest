from flask import render_template, Blueprint, flash, redirect, url_for, request
from app.models import Vote
from app.main.forms import VoteForm
from app import db
from datetime import *
from datetime import timedelta

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def home():
    #form = VoteForm()
    #c='正氣'
    #vote1_btn = Vote(candidates=c)
    #db.session.add(vote1_btn)
    #db.session.commit()
    #Vote.id += 1
    #Vote.vote_id += 1
    #flash('Thanks for Vote!', 'success')
        #return redirect(url_for('main.result'))
    return render_template('index.html', title="Index")

@main.route("/result", methods=['GET'])
def result():
    #result = Vote.query.order_by(Vote.candidates).all()
    m10 = datetime.now() - timedelta(minutes=10)
    c1 = Vote.query.order_by(Vote.candidates.endswith('薯片')).count()
    c2 = Vote.query.filter(Vote.candidates.endswith('林林')).count()
    c3 = Vote.query.filter(Vote.candidates.endswith('正氣')).count()
    c1tenmins = Vote.query.filter(Vote.datetime >= m10).all() and Vote.query.filter(Vote.candidates.endswith('薯片')).count()
    c2tenmins = Vote.query.filter(Vote.datetime >= m10).all() and Vote.query.filter(Vote.candidates.endswith('林林')).count()
    c3tenmins = Vote.query.filter(Vote.datetime >= m10).all() and Vote.query.filter(Vote.candidates.endswith('正氣')).count()
    return render_template('result.html', title='Vote Result', c1=c1, c2=c2, c3=c3, c1tenmins=c1tenmins, c2tenmins=c2tenmins, c3tenmins=c3tenmins)
    