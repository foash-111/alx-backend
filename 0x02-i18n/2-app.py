#!/usr/bin/env python3
"""A simple Flask application demonstrating the use of Flask-Babel
for internationalization (i18n) and localization (l10n).
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app=app)

# Apply the Config class to the app configuration


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


app.config.from_object(Config)


@app.route('/')
def hello():
    """render simple page"""
    greeting = gettext('Hello world')
    return render_template('1-index.html', greeting=greeting)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.

    This function checks the `Accept-Language` header sent by the client
    and selects the best match from the supported languages
    defined in the `Config` class.

    Returns:
        str: The best match language code (e.g., 'en' or 'fr').
    """
    # request.accept_languages.best_match returns
    # the best match for the supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.localeselector(get_locale)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
