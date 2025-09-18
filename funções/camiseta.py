def make_shirt(message, message_lenght='grande'):
	"""Exibe a estampa de uma camisata"""
	print("\nO tamanho da camiseta é " + message_lenght.title() +
	 ", e a estampa é " + message.title() + ".")
	
# make_shirt('eu amo python')
# make_shirt(message_lenght='média', message='Glaucão fortão')
make_shirt('eu amo python', message_lenght='média')
make_shirt('vai chover logo', message_lenght='pequena')


	
