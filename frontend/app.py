import os
import flask

from routes import *

app = flask.Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(movie)
app.register_blueprint(board)


if __name__ == '__main__':
    app.run(debug=True)
