#!/usr/bin/python3
'''Use the module of flask'''
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    text_format = text.replace('_', ' ')
    result = f'Python {text_format}'
    return result


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberOddOrEven(n):

    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template('6-number-odd-or-even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
