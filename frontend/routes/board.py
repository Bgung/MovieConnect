from flask import Blueprint, request, jsonify, render_template

board = Blueprint('board', __name__, url_prefix='/board')

@board.route('/', methods=['GET'])
def get_board_root():
    return render_template('board/index.html')

@board.route('/new_post', methods=['GET', 'POST'])
def get_board_new_post():
    if request.method == 'GET':
        return render_template('board/new_post.html')
    else:
        return jsonify(request.form)

@board.route('/board', methods=['GET'])
def get_board():
    return render_template('board.html')

@board.route('/board', methods=['POST'])
def post_board():
    return jsonify(request.form)

@board.route('/board/<int:board_id>', methods=['GET'])
def get_board_id(board_id):
    return jsonify({'board_id': board_id})

@board.route('/board/<int:board_id>', methods=['PUT'])
def put_board_id(board_id):
    return jsonify({'board_id': board_id})

