logan = {
	'tipo': 'cachorro',
	'nome_dono': 'glauco',
	}

rex = {
	'tipo': 'cachorro',
	'nome_dono': 'jose',
	}
	
laika = {
	'tipo': 'cachorro',
	'nome_dono': 'regiane',
	}
	
pets = [logan, rex, laika]

for pet in pets:
	print(pet['nome_dono'].title() + " é o dono do " + pet['tipo'].title())
	
