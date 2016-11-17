class Cell:

	def __init__(self, bonus=None):
		self._bonus = bonus
		self._bonus_used = False
		self.value = None

	@property
	def bonus(self):
		if not self._bonus_used:
			self._bonus_used = True
			return self._bonus
		return None

	@property
	def busy(self):
		return self.value is not None

def _double_score(data):
	if isinstance(list, data):
		return map(lambda x: x * 2, data)
	if isinstance(int, data):
		return data * 2
	return data

def _triple_score(data):
	if isinstance(list, data):
		return map(lambda x: x * 3, data)
	if isinstance(int, data):
		return data * 3
	return data

class Board:

	size = 15
						# 012345678912345
	_board_definition = ("T__l___T___l__T" # A
						 "_t___L___L___t_" # B
						 "__t___l_l___t__" # C
						 "l__t___l___t__l" # D
						 "____t_____t____" # E
						 "_L___L___L___L_" # F
						 "__l___l_l___l__" # G
						 "T__l___t___l__T" # H
						 "__l___l_l___l__" # I
						 "_L___L___L___L_" # J
						 "____t_____t____" # K
						 "l__t___l___t__l" # L
						 "__t___l_l___t__" # M
						 "_t___L___L___t_" # N
						 "T__l___T___l__T")# O

	@classmethod
	def _get_indexes(cls, s):
		return [i for i, c in enumerate(cls._board_definition) if c in s]

	def _get_cell_bonus(self, position):
		for k, v in self.bonus_definition.items():
			if position in k:
				return v
		return None

	def __init__(self):	
		self.bonus_definition = {
			frozenset(self._get_indexes("lt")): _double_score,
			frozenset(self._get_indexes("LT")): _triple_score,
		}
		self.cells = []
		i = 0
		for _ in range(self.size):
			row = []
			for _ in range(self.size):
				row.append(Cell(self._get_cell_bonus(i)))
				i += 1
			self.cells.append(row)

	def display(self):
		for row in self.cells:
			print('.'.join([' ' if cell.value is None else cell.value for cell in row]))
