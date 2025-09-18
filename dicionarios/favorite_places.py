favorite_places = {
	'glauco': ['frança', 'alemanha'],
	'regiane': ['goiânia', 'frança'],
	'gabriel': ['palmeiras', 'monte carmelo'],
	}
	
# Percorre o dicionário e armazena a chave e o valor que é uma lista.
# O valor é uma lista.	
for name, places in favorite_places.items():	
	print("\nO(s) lugar(es) favorito(s) de " + name.title() + " é: ")
# Esse laço percorre a lista de lugares favoritos de cada pessoa.
	for place in places:
		print("\t" + place.title())

 
