class User():
	"""Classe que modela um usuário."""
	
	def __init__(self, first_name, last_name, idade, sexo):
		"""Ïnicializa os atributos do usuário."""
		self.first_name = first_name
		self.last_name = last_name
		self.idade = str(idade)
		self.sexo = sexo
		self.login_attempts = 0
		
	def describe_user(self):
		"""Descreve as informações do usuário."""
		print("\nO nome do usuário é " + self.first_name.title() + ".")
		print("O último nome do usuário é " + self.last_name.title() + ".")
		print("A idade do usuário é " + self.idade.title() + ".")
		print("O sexo do usuário é " + self.sexo.title() + ".")
		print("O Login attempts é " + str(self.login_attempts) + ".")
		
	def increment_login_attempts(self):
		"""Incrementa o valor de login_attempts em 1"""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""Reinicia o valor de login_attempts em 0"""
		self.login_attempts = 0	
		
	def greet_user(self):
		"""Mostra uma saudação personalizada para o usuário"""
		print("\nOlá " + self.first_name.title() + "! Seja benvindo!")
		
		
# one_user = User('glauco', 'bonturi', '47', 'masculino') 
# one_user.describe_user()
# one_user.greet_user()

other_user = User('gabriel', 'bonturi', '21', 'masculino')
other_user.describe_user()
other_user.greet_user()

other_user.increment_login_attempts()
other_user.increment_login_attempts()
other_user.increment_login_attempts()
other_user.describe_user()
other_user.reset_login_attempts()
other_user.describe_user()
