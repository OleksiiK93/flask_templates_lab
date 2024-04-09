from flask import render_template, Blueprint, request
from models.event_list import events
from models.event import Event
import datetime

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/')
def index():
    return render_template('index.html', events = events)

@events_blueprint.route('/', methods=['POST'])
def add_event():
    name = request.form['name']
    date = datetime.datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    number_of_guests = int(request.form['guests'])
    location = request.form['location']
    description = request.form['description']
    new_event = Event(date, name, number_of_guests, location, description)
    events.append(new_event)
    return render_template('index.html', events = events)