#!/usr/bin/python

from Rounds import Round
from argparse import ArgumentParser
from Utils import *
from Rounds.Utils import *

def main():
	parser = ArgumentParser(description='Analayze demo from csgo by demo_listimportantticks')
	parser.add_argument('file', type=str, help='important ticks file')
	parser.add_argument('-r', '--round', type=int, help='print specific round flow')

	args = parser.parse_args()

	rounds = file_to_rounds(args.file)

	if args.round:
		round = rounds[args.round-1]

		print "\n%s \t%s\n" % (round, round_to_kills(round))
		for event in round.get_real_events():
			print event

	else:
		print "#RoundNum, Round in ticks\tplayer name x amount of kills (amount of headshots)"
		for round in rounds:
			print "%s \t%s" % (round, round_to_kills(round))

if __name__ == "__main__":
	main()
