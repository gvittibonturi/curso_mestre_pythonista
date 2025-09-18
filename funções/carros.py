def make_car(fabricante, modelo, **atributos):
	"""Constrói um dicionário contendo informações sobre um carro"""
	perfil_carro={}
	perfil_carro['carro_fabricante'] = fabricante
	perfil_carro['carro_modelo'] = modelo
	for key, value in atributos.items():
		perfil_carro[key] = value
	return perfil_carro
	
carro = make_car('mercedes bens', 'passeio', cor='preto',
					pacote_sport=True)
					
print(carro)
