#!/usr/bin/env python3
"""
A simple Flask application demonstrating the use of Flask-Babel
for internationalization (i18n) and localization (l10n).
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app=app)

# Apply the Config class to the app configuration
# app.config.from_object('Config')


class Config:
    """
    customize Flask-Babel's behavior by configuring some options
    This sets the default language for your application.
    If no specific language is provided in the URL
    or the user's settings, this locale will be used.
    """
    # app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ["en", "fr"]


@app.route('/')
def hello():
    """render simple page"""
    greeting = gettext('Hello world')
    return render_template('1-index.html', greeting=greeting)

@babel.localeselector
def get_locale():
    return request.accept_language.best_match(app.config['LANGUAGES'])





if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
