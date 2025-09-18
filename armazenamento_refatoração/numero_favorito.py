import json

# Carrega o número favorito se foi armazenado anteriormente
# Caso contrário, pede que o usuário forneça o número favorito e armazena o mesmo




def get_stored_fnumber():
	"""Obtém o número favorito armazenado se estiver disponível."""
	
	filename = 'num_favorito.json'
	try:	
		with open(filename) as f_obj:
			num_favorito = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return num_favorito
	
		
def get_new_number():
	"""Obtém o número favorito do usuário"""
	
	num_favorito = input("\nDigite seu número favorito: ")
	filename = 'num_favorito.json'
	with open(filename, 'w') as f_obj:
		json.dump(num_favorito, f_obj)
	return num_favorito
	
	
def greet_user():
	"""Saúda o usuário pelo nome"""
	
	num_favorito = get_stored_fnumber()
	if num_favorito:
		print("Eu sei qual é o seu número favorito! É " + num_favorito + ".")
	else:
		num_favorito = get_new_number()
		print("Nós vamos lembrar do seu número favorito quando você voltar: " + num_favorito + ".")
		
greet_user()
		


#print("Eu sei qual é o seu número favorito! É " + num_favorito + ".")
