from flask import render_template, Blueprint, flash, redirect, url_for, request, json, jsonify
from app.models import Vote
from app import db
from datetime import *
from datetime import timedelta


main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def home():
    return render_template('index.html', title='Index')

@main.route("/vote", methods=['POST'])
def vote():
    vote_btn = Vote(candidates=json.loads(request.data)['candidate']) 
    db.session.add(vote_btn)
    db.session.commit()
    Vote.vote_id += 1
    return jsonify('ok'), render_template('index.html', title='Index')

@main.route("/result", methods=['GET'])
def result():
    ''' Count candidates '''
    c1 = Vote.query.filter(Vote.candidates.endswith('薯片')).count()
    c2 = Vote.query.filter(Vote.candidates.endswith('林林')).count()
    c3 = Vote.query.filter(Vote.candidates.endswith('正氣')).count()
    ''' Find last 10mins result '''
    m10 = datetime.now() - timedelta(minutes=10)
    c1tenmins = Vote.query.filter(Vote.datetime >= m10).filter(Vote.candidates == '薯片').count()
    c2tenmins = Vote.query.filter(Vote.datetime >= m10).filter(Vote.candidates == '林林').count()
    c3tenmins = Vote.query.filter(Vote.datetime >= m10).filter(Vote.candidates == '正氣').count()
    
    return render_template('result.html', title='Vote Result', c1=c1, c2=c2, c3=c3, c1tenmins=c1tenmins, c2tenmins=c2tenmins, c3tenmins=c3tenmins)