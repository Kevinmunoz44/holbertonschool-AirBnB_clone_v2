#!/usr/bin/python3
'''Use the module of flask'''
from flask import Flask
'''
Initializate this application with flask
'''

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text_format = text.replace('_', ' ')
    result = f'C {text_format}'
    return result


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    text = 'is cool'
    text_format = text.replace('_', ' ')
    result = f'Python {text_format}'
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
