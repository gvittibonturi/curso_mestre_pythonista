#usuarios = ['Glauco', 'Antônio', 'Silvia', 'Pamela', 'Admin']
usuarios = []

if usuarios:
	for usuario in usuarios:
		if usuario == 'Admin':
			print("\nOlá " + usuario + ", gostaria de ver um relatório de status?")
		else:
			print("\nOlá " + usuario + ", obrigado por fazer login novamente")
else:
	print("Precisamos encontrar alguns usuários!")
