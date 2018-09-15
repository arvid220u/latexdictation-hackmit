#!/usr/bin/env python3
from flask import *
app = Flask(__name__)


# IMPORTANT THINGS START HERE

@app.route("/")
def home():
    return app.send_static_file('static/index.html')

from main import text2latex
@app.route("/api/<text>")
def API(text):
    return text2latex(text)
