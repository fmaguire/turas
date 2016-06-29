#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

app.config.from_object('config')

import turas.views
