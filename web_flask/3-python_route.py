#!/usr/bin/python3
# a script that starts a Flask web application

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ print hello world """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” and free-text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ” with free-text"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)