from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
stores = [
    {'name': 'My Store',
    'items': [
        {
            'name': 'Chair',
            'price': 10.00
        }
    ],

    }
]