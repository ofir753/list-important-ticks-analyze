#!/usr/bin/python

from Rounds import Round
from argparse import ArgumentParser
from Utils import *
from Rounds.Utils import *

def main():
	parser = ArgumentParser(description='Analayze demo from csgo by demo_listimportantticks')
	parser.add_argument('file', type=str, help='important ticks file')

	args = parser.parse_args()

	analyze(args.file)

def analyze(filename):
	rounds = file_to_rounds(filename)

	print "#RoundNum, Round in ticks\tplayer name x amount of kills (amount of headshots)"
	for round in rounds:
		print "%s \t%s" % (round, round_to_kills(round))

if __name__ == "__main__":
	main()
