#!/usr/bin/env python3

'''
Install the Babel Flask extension
```sh
pip3 install flask_babel
```
Then instantiate the `Babel` object in your app. Store it in a module-level
variable named `babel`.

In order to configure available languages in our app, you will
create a `Config` class that has a `LANGUAGES` class attribute
equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.
'''

from flask import Flask
from flask import render_template
from flask_babel import Babel
from typing import Any


app = Flask(__name__)
babel = Babel(app)


class Config:
    """docstring for Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def home_page() -> Any:
    '''Returns homepage'''
    return render_template('1-index.html')
