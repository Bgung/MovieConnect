from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def root():
    return render_template("index.html")
