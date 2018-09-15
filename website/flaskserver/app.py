#!/usr/bin/env python3
import random, os, sys, binascii
import subprocess
import sqlite3
from hashlib import md5
from base64 import b64encode
from datetime import datetime
import time
import config as turingconfig

from flask import *
app = Flask(__name__)
app.config.from_object(__name__) # configure from this file
app.config["SECRET_KEY"] = turingconfig.FLASK_SECRET_KEY
#HTTPS
app.config["PREFERRED_URL_SCHEME"] = "https"

# apparently this is for safety of some sort
def rlpt(pt):
    return os.path.join(app.root_path, pt)



# DATABASE
app.config["DATABASE"] = rlpt("app.db")

def connect_db():
    # use detect_types for easy datetime
    rv = sqlite3.connect(app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
    rv.row_factory = sqlite3.Row
    return rv

# get database
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# tear down database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()






# IMPORTANT THINGS START HERE



@app.route("/")
def home():



    return "hej"


