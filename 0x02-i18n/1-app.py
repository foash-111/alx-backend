#!/usr/bin/env python3
"""instantiate the Babel object in your app."""

from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app=app)


class Config:
    """
    customize Flask-Babel's behavior by configuring some options
    This sets the default language for your application.
    If no specific language is provided in the URL
    or the user's settings, this locale will be used.
    """
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
    LANGUAGES = ["en", "fr"]


@app.route('/')
def hello():
    """render simple page"""
    greeting = gettext('Hello world')
    return render_template('1-index.html', greeting=greeting)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
