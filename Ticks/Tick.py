#!/usr/bin/python

from Event import Event
from Kill import Kill

class Tick(object):

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
			return Event(parts)
		else:
			return Kill(parts)

