#!/usr/bin/python3
"""
flask web app
"""

from flask import Flask, render_template
from models import *
from models import storage


@app.route('/states_list', strict_slashs=False)
def states_list():
    """display a HTML page woth the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").value()), key=lamba x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
