from flask import Flask, send_from_directory
from database import connect_db
from model import model_get_currencies, model_get_pairs

import json
import os

app = Flask(__name__, static_folder=os.path.abspath("."))


@app.route("/")
def root():
    return app.send_static_file("res/pages/index.html")


@app.route("/res/<path:path>")
def send_resource(path):
    print("static: %s" % path)
    return send_from_directory("res", path)


@app.route("/api/currencies")
def currencies():
    with connect_db() as conn:
        currencies = model_get_currencies(conn)
        return json.dumps(currencies)


@app.route("/api/pairs")
def pairs():
    with connect_db() as conn:
        pairs = model_get_pairs(conn)
        return json.dumps(pairs)
