from flask import Flask,request

app = Flask(__name__)

# @app.route('/')
# def index():
stores = [
    {'name': 'My Store',
    'items': [
        {
            'name': 'Chair',
            'price': 10.99
        },
        {
            'name': 'Rug',
            'price': 100.67
        }
    ],

    }
]

@app.get('/store')
def get_stores():
    return {'stores':stores}

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'],'items':[]}
    stores.append(new_store)
    return new_store, 201 

