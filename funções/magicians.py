def show_magicians(magicians_names):
	"""Mostra os nomes de todos os mágicos."""
	print("\nO nome do mágico é:")
	for magic in magicians_names:
		print(magic.title())
	
magicos = ['mr. M', 'nosferatu', 'vacile']

show_magicians(magicos)

