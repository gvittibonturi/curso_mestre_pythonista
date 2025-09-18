class Car():
	"""Representação de um carro"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + "miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
		
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
"""Uma classe que pode ser usada para representar um carro."""

class Battery():
	"""Modelagem de uma bateria para um carro elétrico"""
	
	def __init__(self, battery_size=70):
		"""Inicializa os atributos da bateria."""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Exibe uma frase que descreve a capacidade da bateria"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
		
	def get_range(self):
		"""Exibe a frase sobre a distância que o carro é capaz de percorrer
		com essa bateria."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
									
class ElectricCar(Car):
	"""Repreenta aspectos específicos de um carro elétrico."""
	
	def __init__(self, make, model, year):
		"""Inicializa os atributos da classe pai."""
		super().__init__(make, model, year)
		self.battery = Battery()
		

my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


