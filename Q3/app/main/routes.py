from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def home():
    return render_template('index.html', title="Index")


@main.route("/result")
def about():
    return render_template('result.html', title='Vote Result')