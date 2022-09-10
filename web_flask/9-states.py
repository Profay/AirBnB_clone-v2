#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display lists of State"""
    list_state = storage.all(State).values()
    return render_template('7-states_list.html', list_state=list_state)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """display lists all State and all cities for State"""
    list_state = storage.all(State).values()
    for state in list_state:
        if state.id == id:
            return render_template('9-states.html', states=state, id=True)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
