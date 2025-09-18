def describe_city(city_name, country='Brasil'):
	"""Exibe uma mensagem sobre a cidade"""
	print("\n" + city_name.title() + " está localizado(a) no(a) " +
	 country.title())
	
describe_city('goiânia')
describe_city('são paulo')
describe_city('paris', country='frança')

