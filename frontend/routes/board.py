import requests

from flask import Blueprint, request, jsonify, render_template

board = Blueprint('board', __name__, url_prefix='/board')

@board.route('/', methods=['GET'])
def get_board_root():
    response = requests.get('http://api-gateway:9090/posts')
    return render_template(
       'board/index.html',
       header="KMJAE's Board",
       board_title='게시판',
       posts=response.json()
    )

@board.route('/post/<string:post_id>', methods=['GET'])
def get_board_post(post_id: str):
    response = requests.get(f'http://api-gateway:9090/posts/{post_id}')
    return render_template(
        'board/post.html',
        header="KMJAE's Board",
        board_title='게시판',
        post=response.json()
    )

@board.route('/new_post', methods=['GET'])
def get_board_new_post():
    print('New post page')
    return render_template('board/new_post.html')

@board.route('/new_post', methods=['POST'])
def post_board_new_post():
  # API Server에 post 요청
  title = request.form['title']
  content = request.form['content']
  author = request.form['author']
  response = requests.post('http://api-gateway:9090/posts', json={
    'title': title,
    'content': content,
    'author': author
  }).json()
  if response['status_code'] == 201:
    return get_board_root()
  else:
    return jsonify(response)