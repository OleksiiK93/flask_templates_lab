from models.event import Event
import datetime

event1 = Event(datetime.date(2024, 4, 15), "Annual Gala Dinner", 200, "Grand Ballroom", "A formal dinner celebrating our achievements.")
event2 = Event(datetime.date(2024, 6, 20), "Tech Conference", 500, "Conference Hall A", "Bringing together tech enthusiasts and experts for talks and workshops.")
event3 = Event(datetime.date(2024, 8, 10), "Company Retreat", 50, "Mountain Lodge", "A team-building retreat in the mountains for employees.")
event4 = Event(datetime.date(2024, 9, 5), "Product Launch", 100, "Event Space", "Unveiling our latest product with demonstrations and presentations.")
event5 = Event(datetime.date(2024, 11, 18), "Charity Fundraiser", 300, "Community Center", "Raising funds for a local charity with auctions and performances.")

events = [event1, event2, event3, event4, event5]