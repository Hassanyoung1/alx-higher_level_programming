#!/usr/bin/python3
"""
a script that starts a Flask web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(_name_)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a HTML page with a list of all State objects """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
