from collections import defaultdict
import operator
from Round import Round
from Events import Kill

def round_to_kills(round):
	player_to_kills = defaultdict(int)
	player_to_hs = defaultdict(int)

	kills = filter(lambda event: isinstance(event, Kill), round.events)


	for kill in kills:
		player_to_kills[kill.attacker] += 1
		if kill.hs:
			player_to_hs[kill.attacker] += 1

	player_to_kills = dict(player_to_kills)
	player_to_kills = sorted(player_to_kills.items(), key=operator.itemgetter(1), reverse=True)

	kills_string =  ', '.join(map(lambda player: "%s x%d(%d)" % (player[0], player[1], player_to_hs[player[0]]), player_to_kills))

	return kills_string