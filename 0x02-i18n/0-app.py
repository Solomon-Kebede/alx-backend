#!/usr/bin/env python3

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('0-index.html')