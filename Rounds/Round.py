
from collections import defaultdict
from Events import Kill
import operator

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
	
	def analyze_round(self):
		player_to_kills = defaultdict(int)
		player_to_hs = defaultdict(int)

		kills = filter(lambda event: isinstance(event, Kill), self.events)

		for kill in kills:
			player_to_kills[kill.attacker] += 1
			if kill.hs:
				player_to_hs[kill.attacker] += 1

		player_to_kills = dict(player_to_kills)
		player_to_kills = sorted(player_to_kills.items(), key=operator.itemgetter(1), reverse=True)
	
		kills_string =  ', '.join(map(lambda player: "%s x%d(%d)" % (player[0], player[1], player_to_hs[player[0]]), player_to_kills))

		return kills_string


