def show_magicians(magicians_names):
	"""Mostra os nomes de todos os mágicos."""
	print("\nO nome do mágico é:")
	for magic in magicians_names:
		print(magic.title())
		
def make_great(magic_names, big_magic):
	"""Acrescenta uma expressão ao nome."""
	while magic_names:
		current_magic = magic_names.pop()
		
		# Simula a criação de uma lista de grandes mágicos
		# print("O Grande " + current_magic)
		big_magic.append(current_magic)
	return (big_magic)
		
	
magicos = ['mr. M', 'nosferatu', 'vacile']
big_magic = []

inaltereted_ones = make_great(magicos[:], big_magic)
# show_magicians(magicos)
# show_magicians(big_magic)

show_magicians(inaltereted_ones)
show_magicians(big_magic)
