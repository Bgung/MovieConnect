import flask
import markdown

from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def root():
    with open('./static/md/introduce.md', "r") as f:
        markdown_content = f.read()
        markdown_html = markdown.markdown(markdown_content)
    return render_template("index.html", markdown_content=markdown_html)
