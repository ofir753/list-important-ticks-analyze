#!/usr/bin/python

from Event import Event
from Kill import Kill

class Factory(object):

	@staticmethod
	def factory(line):
		if not line.startswith("Tick: "):
			raise Exception("Not an important tick string")

		line = line.strip()
		parts = line.split(":")

		if len(parts) != 3:
			raise Exception("Not an important tick string")

		parts = map(lambda part: part.strip(), parts)

		if "Event" in parts[1]:
			e = Event()
			e.init_event_by_parts(parts)
			return e
		else:
			return Kill(parts)
