#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a list of all State objects"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays a list of all State objects with their cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the database after process"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)