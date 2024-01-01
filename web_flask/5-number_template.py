#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Returns text"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """Return text"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """replace text with variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """replace more texts with variables"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """replace text with an int"""
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """display html if n is an int"""
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
