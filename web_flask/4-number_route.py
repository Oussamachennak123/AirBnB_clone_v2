#!/usr/bin/python3
""" application flask """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def is_cool(text='is cool'):
    return "Python " + text.replace('_', ' ')


@app.route('/number', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def n():
    if isinstance(n, int):
        return n
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
