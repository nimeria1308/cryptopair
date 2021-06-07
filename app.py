from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_folder=os.path.abspath("."))


@app.route("/")
def root():
    return app.send_static_file("pages/index.html")


@app.route("/res/<path:path>")
def send_resource(path):
    print("static: %s" % path)
    return send_from_directory("res", path)

# API used for requesting data from database


@app.route("/test")
def test_r():
    print("test")
    return "hello???"
