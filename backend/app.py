import socket

from fastapi import FastAPI
from contextlib import asynccontextmanager

from models.mongodb import Post

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server running at {socket.gethostbyname(socket.gethostname())} Hostname={socket.gethostname()}", flush=True)
    yield
    print("Stopping", flush=True)

app = FastAPI(lifespan=lifespan)

@app.get('/')
def read_root():
    return {'Hello': f'World from {socket.gethostbyname(socket.gethostname())} {socket.gethostname()}'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}

@app.post('/items/')
def create_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


@app.get('/posts/')
def read_post(n: int = 10):
    post = Post.Post()
    response = post.find_all()
    response = [
        {str(k): str(v) for k, v in doc.items()} for doc in response
    ]
    return response

@app.get('/posts/{item_id}')
def read_post(item_id: str):
    post = Post.Post()
    response = post.find_by_id(item_id)
    response = {str(k): str(v) for k, v in response.items()}
    print("update", post.update({'_id': item_id}, {'$inc': {'views': 1}}))
    return response

@app.post('/posts/')
def create_post(data: dict):
    post = Post.Post()
    response = post.insert(data)
    if response.acknowledged:
        return {'status_code': 201, 'message': 'Created'}
    else:
        return {'status_code': 500, 'message': 'Internal Server Error'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host='0.0.0.0', port=8080, reload=True)