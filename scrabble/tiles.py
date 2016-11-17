from random import shuffle

class Tile:

	def __init__(self, letter, value):
		self.letter = letter
		self.value = value

	def __str__(self):
		return self.letter

	def __repr__(self):
		return (self.letter + str(self.value))

class Tiles:

	_letter_repartition = {
		1: "JQKWXYZ",
		2: "?FHVBCPG",
		3: "DM",
		5: "L",
		6: "UTSRON",
		8: "I",
		9: "A",
		15: "E"
	}
	_letter_values = {
		0: "?",
		1: "EAINORSTUL",
		2: "DMG",
		3: "BCP",
		4: "FHV",
		8: "JQ",
		10: "KWXYZ"
	}

	def _get_letter_value(self, c):
		for k, v in self._letter_values.items():
			if c in v:
				return k
		return 0

	def __init__(self):
		self.pool = [Tile(c, self._get_letter_value(c))
						for k, v in self._letter_repartition.items()
						for c in v
						for _ in range(k)]
		shuffle(self.pool)
