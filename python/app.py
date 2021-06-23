from flask import Flask, send_from_directory
from database import connect_db
from model import *

import json
import os

app = Flask(__name__, static_folder=os.path.abspath("res/"))


@app.route("/")
def root():
    return app.send_static_file("pages/index.html")


@app.route("/res/<path:path>")
def send_resource(path):
    print("static: %s" % path)
    return send_from_directory(app.static_folder, path)


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


@app.route("/api/pair/<int:pair_id>/year")
def bids_by_year(pair_id):
    with connect_db() as conn:
        bids = model_get_bids_by_year(conn, pair_id)
        return json.dumps(bids)


@app.route("/api/pair/<int:pair_id>/month/<int:year>")
def bids_by_month(pair_id, year):
    with connect_db() as conn:
        bids = model_get_bids_by_month(conn, pair_id, year)
        return json.dumps(bids)


@app.route("/api/pair/<int:pair_id>/day/<int:year>/<int:month>")
def bids_by_day(pair_id, year, month):
    with connect_db() as conn:
        bids = model_get_bids_by_day(conn, pair_id, year, month)
        return json.dumps(bids)
