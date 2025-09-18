# def get_city_country(city_name, country_name):
#	"""Devolve um dicionário com a cidade e seu país"""
#	city_and_country = {'city': city_name, 'country': country_name}
#	city_and_country['city'] = city_and_country['city'].title()
#	city_and_country['country'] = city_and_country['country'].title()
#	city_country_formated = city_and_country['city'] + ',' + ' ' + city_and_country['country']
#	return city_and_country
	
def get_city_country(city_name, country_name):
	"""Devolve uma cidade e seu país formatados de forma elegante"""
	city_and_country = city_name + ',' + ' ' + country_name
	return city_and_country.title()


city_country = get_city_country('"goiânia', 'goiás"')
print(city_country)

city_country = get_city_country('rio claro', 'são paulo')
print(city_country)

city_country = get_city_country('"guapó"', '"goiás"')
print(city_country)
