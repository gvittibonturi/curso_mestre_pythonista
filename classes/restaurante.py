"""Módulo Restaurante"""

class Restaurant():
	"""Classe que modela um restaurante."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos restaurant_name e cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""Descreve o nome e tipo de cozinha do restaurante"""
		print("O nome do restaurante é " + self.restaurant_name.title() + ".")
		print("O tipo de cozinha do restaurante é " +

	self.cuisine_type.title() + ".")
		
	def open_restaurant(self):
		"""Exibe uma mensagem informando que o restaurante está aberto"""
		print("O restaurante " + self.restaurant_name + " está aberto.")
		

class User():
	"""Classe que modela um usuário."""
	
	def __init__(self, first_name, last_name, idade, sexo):
		"""Ïnicializa os atributos do usuário."""
		self.first_name = first_name
		self.last_name = last_name
		self.idade = str(idade)
		self.sexo = sexo
		
	def describe_user(self):
		"""Descreve as informações do usuário."""
		print("\nO nome do usuário é " + self.first_name.title() + ".")
		print("O último nome do usuário é " + self.last_name.title() + ".")
		print("A idade do usuário é " + self.idade.title() + ".")
		print("O sexo do usuário é " + self.sexo.title() + ".")
		
	def greet_user(self):
		"""Mostra uma saudação personalizada para o usuário"""
		print("\nOlá " + self.first_name.title() + "! Seja benvindo!")
		



