from enum import IntEnum

cs_events_strings = [
"round_end",
"cs_pre_restart",
"round_start",
"round_freeze_end",
"bomb_dropped",
"bomb_pickup",
"bomb_beginplant",
"bomb_planted",
"bomb_begindefuse",
"bomb_defused",
"bomb_exploded"
]

to_string_events = [
"Round End",
"Round Pre Restart",
"Round Start",
"Round FreezeEnd",
"Bomb Dropped",
"Bomb Picked",
"Bomb BeginPlant",
"Bomb Planted",
"Bomb BeingDefuse",
"Bomb Defused",
"Bomb Exploded",
"Undefined"
]

class EEvent(IntEnum):
	RoundEnd = 0
	RoundPreRestart = 1
	RoundStart = 2
	RoundFreezeEnd = 3
	BombDropped = 4
	BombPicked = 5
	BombBeginPlant = 6
	BombPlanted = 7
	BombBeingDefuse = 8
	BombDefused = 9
	BombExploded = 10
	Undefined = 11

def event_from_string(string):
	if string not in cs_events_strings:
		return EEvent.Undefined

	return EEvent(cs_events_strings.index(string))

def event_to_string(event):
	if event > EEvent.Undefined:
		return to_string_events[EEvent.Undefined]

	return to_string_events[event]
