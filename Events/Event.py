
from EEvent import EEvent, event_from_string, event_to_string

class Event():
	def __init__(self, type = EEvent.Undefined):
		self.type = type

	def init_event_by_parts(self, parts):
		self.tick = int(filter(lambda c: c.isdigit(), parts[1]))
		self.type = event_from_string(parts[2])

	def __str__(self):
		return "Tick: %d, Event: %s" % (self.tick, event_to_string(self.type))

	def __repr__(self):
		return str(self)