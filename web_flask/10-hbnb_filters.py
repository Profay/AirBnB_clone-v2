#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def cities():
    """ Function that return list of states and amenities """
    list_amenity = storage.all(Amenity).values()
    list_state = storage.all(State).values()
    return render_template('10-hbnb_filters.html', list_state=list_state,
                           list_amenity=list_amenity)


@app.teardown_appcontext
def teardown_db(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
