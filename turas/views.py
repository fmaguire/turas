#!/usr/bin/env python3

from turas import app
from .forms import LocationForm
import flask

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("index.html")

@app.route('/start', methods=['GET', 'POST'])
def start():
    """
    view for data entry for optimisation
    """
    form = LocationForm()
    if form.validate_on_submit():
        return optimise(form.data)

    return flask.render_template("start.html",
                                 title="Start", form=form)

@app.route('/previous', methods=['GET', 'POST'])
def previous():
    """
    getting previous results
    """
    pass

def optimise(data):
    return flask.render_template('processing.html', data=data)


@app.route('/results')
def results():
    return flask.render_template('results.html')


