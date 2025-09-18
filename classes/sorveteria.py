class Restaurant():
	"""Classe que modela um restaurante."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos restaurant_name e cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.flavors = flavors = ['creme', 'chocolate', 'morango', 'limão'] 
	
	def describe_restaurant(self):
		"""Descreve o nome e tipo de cozinha do restaurante"""
		print("O nome do restaurante é " + self.restaurant_name.title() + ".")
		print("O tipo de cozinha do restaurante é " +
				self.cuisine_type.title() + ".")
				
	def describe_flavors(self):
		for flavor in self.flavors:
			print("Os sabores disponíveis são: " + flavor + ".")
		
		
	def open_restaurant(self):
		"""Exibe uma mensagem informando que o restaurante está aberto"""
		print("O restaurante " + self.restaurant_name + " está aberto.")
		
		
my_restaurant = Restaurant("bonturi's", "italiana")
yours_restaurant = Restaurant("silva's", "basco")
hes_restauratnt = Restaurant("olivers", "francês")

#print(" O nome do meu restaurante é: " +
# my_restaurant.restaurant_name.title() + ".")
#print(" O tipo de cozinha do meu restaurante é: " +
# my_restaurant.cuisine_type.title() + ".")

#my_restaurant.describe_restaurant()
#yours_restaurant.describe_restaurant()
#hes_restauratnt.describe_restaurant()
#my_restaurant.open_restaurant()

class IceCreamStand(Restaurant):
	"""Representa aspectos de um restaurante epsecíficos de sorveteria"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa os atributos da classe pai"""
		super().__init__(restaurant_name, cuisine_type)
		
my_icecreamstand = IceCreamStand("Glauco's", "Italiana")
print(my_icecreamstand.describe_restaurant())
print(my_icecreamstand.describe_flavors())
