#!/usr/bin/python3
'''Use the module of flask'''
from flask import Flask
'''
Initializate this application with flask
'''

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
