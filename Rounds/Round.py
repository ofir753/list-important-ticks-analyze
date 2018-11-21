
from Events import Kill

class Round():
	def __init__(self, start_tick, round_num):
		self.start_tick = start_tick
		self.end_tick = 0
		self.round_num = round_num
		self.events = []

	def set_end(self, end_tick):
		self.end_tick = end_tick

	def add_event(self, event):
		self.events.append(event)

	def set_roundnum(self, round_num):
		self.round_num = round_num

	def __str__(self):
		return "#%s, Range: %d - %d" % (self.round_num, self.start_tick, self.end_tick)

	def print_events(self):
		for event in self.events:
			print event


