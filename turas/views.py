#!/usr/bin/env python3

from turas import app

@app.route('/')
def index():
    return "Start Page"
