from Events import Factory, Event, Kill
from Events.EEvent import *
from Rounds import Round

def file_to_events(filename):
	events = []

	with open(filename) as f:
		lines = f.readlines()

		for line in lines:
			events.append(Factory.factory(line))

	return events

def extract_rounds(events):
	rounds = []

	round_num = 1
	current_round = Round(0, round_num)

	for event in events:
		if event.type == EEvent.RoundStart:
			current_round = Round(event.tick, round_num)

		elif event.type == EEvent.RoundPreRestart:
			current_round.set_end(event.tick)

			# In case of restart round
			if current_round in rounds:
				rounds.remove(current_round)
			else:
				round_num += 1
				
			rounds.append(current_round)

		
		current_round.add_event(event)

	return rounds

pistols = [
"usp",
"usp_silencer",
"glock",
"hkp2000",
"p250",
"deagle",
"tec9",
"cz75a",
"fiveseven",
"elite",
"revolver",
"world"
]

def find_pistol_round(rounds):
	for round in rounds:
		kills = filter(lambda event: isinstance(event, Kill), round.events)
		weapons = map(lambda kill: kill.weapon, kills)
		weapons = filter(lambda weapon: weapon != "world", weapons)
		not_pistols = filter(lambda weapon: weapon not in pistols, weapons)

		if len(not_pistols) == 0 and len(weapons) != 0:
			return round

	return rounds[0]

def find_pistol_round_by_tick(rounds, tick):
	rounds = filter(lambda round: round.start_tick == tick, rounds)

	return rounds[0]

def fix_rounds(rounds, pistol_round_tick):
	if pistol_round_tick == None:
		pistol_round = find_pistol_round(rounds)
	else:
		pistol_round = find_pistol_round_by_tick(rounds, pistol_round_tick)

	rounds = rounds[rounds.index(pistol_round):]
	rounds = filter(lambda round: len(round.get_real_events()) > 0, rounds)

	counter = 1
	for round in rounds:
		round.set_roundnum(counter)
		counter += 1


	return rounds

def file_to_rounds(filename, pistol_round_tick=None):
	events = file_to_events(filename)
	rounds = extract_rounds(events)
	rounds = fix_rounds(rounds, pistol_round_tick)

	return rounds
