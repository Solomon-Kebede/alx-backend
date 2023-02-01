#!/usr/bin/env python3

'''
Create a `get_locale` function with the `babel.localeselector decorator`.
Use `request.accept_languages` to determine the best match with our
supported languages.
'''

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask_babel import Babel
from typing import Any


app = Flask(__name__)
babel = Babel(app)


class Config:
    """docstring for Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home_page() -> Any:
    '''Returns homepage'''
    return render_template('2-index.html')
