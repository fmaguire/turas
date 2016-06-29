#!/usr/bin/env python3

from turas import app
import flask

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("index.html")

@app.route('/test')
def test():
    return flask.render_template("test.html")
