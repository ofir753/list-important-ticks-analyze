
from Event import Event
from EEvent import EEvent

class Kill(Event):
	def __init__(self, parts):
		self.tick = int(parts[1])
		self.type = EEvent.PlayerDeath
		killstring = parts[2]

		if "with" in killstring:
			attacker_victim, kill_type = killstring.split("with")
			self.hs = True

		else:
			attacker_victim, kill_type = killstring.split("using")
			kill_type = "using" + kill_type
			self.hs = False

		attacker, victim = attacker_victim.split("killed")
		self.attacker, self.victim = attacker.strip(), victim.strip()
		self.weapon = kill_type.split("using a ")[1]

	def __str__(self):
		return str("Tick: %d Attacker: %s, Victim: %s, Weapon: %s, HS: %s" %
				(self.tick, self.attacker, self.victim, self.weapon, self.hs))

	def __repr__(self):
		return str(self)