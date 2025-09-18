pessoas_trabalho = {
	'first_name': 'antônio',
	'last_name': 'albino',
	'age': '35',
	'city': 'goiânia',
	}
	
pessoas_familiares = {
	'first_name': 'regiane',
	'last_name': 'medeiros',
	'age': '39',
	'city': 'goiânia',
	}

pessoas_escola = {
	'first_name': 'ennio',
	'last_name': 'danesi',
	'age': '36',
	'city': 'goiânia',
	}

# Cria uma lista de dicionários
people = [pessoas_trabalho, pessoas_familiares, pessoas_escola]

# Percorre cada dicionário dentro da lista e imprime na tela as informações
for pessoa in people:
	print(pessoa['first_name'].title())
	print(pessoa['last_name'].title())
	print(str(pessoa['age'].title()))
	print("\n")
	
print("...")



