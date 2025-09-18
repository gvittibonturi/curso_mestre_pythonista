class Restaurant():
	"""Classe que modela um restaurante."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos restaurant_name e cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = str(0)
	
	def describe_restaurant(self):
		"""Descreve o nome e tipo de cozinha do restaurante"""
		print("O nome do restaurante é " + self.restaurant_name.title() + ".")
		print("O tipo de cozinha do restaurante é " + self.cuisine_type.title() + ".")
		
	def describe_clients(self):
		"""Descreve o número de clientes atendoiso"""
		print("O numero de clientes atendidos hoje é " + str(self.number_served))
		
	def set_number_served(self, new_served):
		"""Atualiza o número de clientes atendidos"""
		self.number_served = new_served
		
	def increment_number_served(self, inc_served):
		"""Incrementa numero de clientes servidos"""
		self.number_served += inc_served
		
	def open_restaurant(self):
		"""Exibe uma mensagem informando que o restaurante está aberto"""
		print("O restaurante " + str(self.restaurant_name) + " está aberto.")

restaurant = Restaurant('Rufinos', 'Italiana')
restaurant.describe_clients()
restaurant.set_number_served(103)
restaurant.describe_clients()
restaurant.increment_number_served(50)
restaurant.describe_clients()

