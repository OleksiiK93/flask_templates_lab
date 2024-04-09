from flask import render_template, Blueprint, request
from models.event_list import events
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/')
def index():
    return render_template('index.html', events = events)