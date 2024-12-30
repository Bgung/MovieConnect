from flask import Blueprint, render_template

movie = Blueprint('movie', __name__, url_prefix='/movie')

@movie.route('/')
def root():
    return render_template("movie.html")
