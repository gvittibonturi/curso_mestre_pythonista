def make_sanduiche(*itens):
	"""Exibe a lista de ingredientes pedidos"""
	print("\nFazendo um sanduiche com os seguintes iten:")
	for iten in itens:
		print("- " + iten)
	
make_sanduiche('presunto')
make_sanduiche('queijo', 'presunto', 'ovo')


