from random import randint

class Die():
	"""Uma classe"""

	def __init__(self, sides=6):
		"""Inicializa os atributos"""
		self.sides = sides
	
	def roll_die(self):
		"""joga o dado"""
		aleatorio = randint(1, self.sides)
		return aleatorio
	
dado = Die(6)
print("Valor da jogada: " + str(dado.roll_die()))

for num in range(1,10):
	dado = Die(10)
	print("Valor da jogada: " + str(dado.roll_die()))

