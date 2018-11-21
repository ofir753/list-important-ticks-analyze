#!/usr/bin/python

from Ticks import Tick, Event, Kill
from Ticks.EEvent import *
from Rounds import Round, Score
from argparse import ArgumentParser

def file_to_ticks(filename):
	ticks = []

	with open(filename) as f:
		lines = f.readlines()

		for line in lines:
			ticks.append(Tick.factory(line))

	return ticks

def extract_rounds(ticks):
	rounds = []

	round_num = 1
	current_round = Round(0, round_num)

	for tick in ticks:
		if isinstance(tick, Event):
			if tick.event == EEvent.RoundStart:
				current_round = Round(tick.tick, round_num)

			elif tick.event == EEvent.RoundPreRestart:
				current_round.set_end(tick.tick)

				# In case of restart round
				if current_round in rounds:
					rounds.remove(current_round)
				else:
					round_num += 1
					
				rounds.append(current_round)

		
		current_round.add_tick(tick)

	return rounds

pistols = [
"usp",
"usp_silencer",
"glock",
"hkp2000",
"p2000",
"world"
]

def find_pistol_round(rounds):
	for round in rounds:
		kills = filter(lambda tick: isinstance(tick, Kill), round.ticks)
		weapons = map(lambda kill: kill.weapon, kills)
		weapons = filter(lambda weapon: weapon != "world", weapons)
		not_pistols = filter(lambda weapon: weapon not in pistols, weapons)

		if len(not_pistols) == 0 and len(weapons) != 0:
			return round

	return rounds[0]

def set_pistol_round(rounds):

	pistol_round = find_pistol_round(rounds)
	rounds = rounds[rounds.index(pistol_round):]

	counter = 1
	for round in rounds:
		round.set_roundnum(counter)
		counter += 1

	return rounds

def analyze(filename):
	ticks = file_to_ticks(filename)
	rounds = extract_rounds(ticks)
	rounds = set_pistol_round(rounds)


	print "#RoundNum, Round in ticks\tplayer name x amount of kills (amount of headshots)"
	for round in rounds:
		print "%s \t%s" % (round, round.analyze_round())

if __name__ == "__main__":
	parser = ArgumentParser(description='Analayze demo from csgo by demo_listimportantticks')
	parser.add_argument('file', type=str,
					   help='important ticks file')

	args = parser.parse_args()

	analyze(args.file)
