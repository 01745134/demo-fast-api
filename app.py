import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def hello_world():
    return {'message': 'Hello, World!'}

@app.get('/spanish/')
def hello_spanish():
    return {'message': 'Hola, Mundo!'}

@app.get('/{name}')
def hello_name(name: str):
    return {'message': f'HellO {name}'}