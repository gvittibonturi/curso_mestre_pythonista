"""Módulo de usuários e privilégios"""

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
		
			
class Privileges():
	"""Privilégios para o Admin - classe separada"""
	
	def __init__(self):
		"""Inicializa atributos"""
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def show_privileges(self):
		for privilege in self.privileges:
			print("Os privilégios de admin são: " + privilege + ".")
		
		
class Admin(User):
	"""Uma classe que vai herdar da classe User"""
	
	def __init__(self, first_name, last_name, idade, sexo):
		"""Inicialializa os atributos da classe pai"""
		super().__init__(first_name, last_name, idade, sexo)
		self.privileges = Privileges()
		
		

