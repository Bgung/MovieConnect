import os
import socket

import flask

from routes import *

app = flask.Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(movie)
app.register_blueprint(board)

if __name__ == '__main__':
    print(f"Server running on {socket.gethostbyname(socket.gethostname())} Hostname={socket.gethostname()}")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
