cities = {
	'paris': {
		'country': 'frança',
		'population': '5000000',
		'fact': 'histórica',
		'infra': 'rail',
	},
	
	'goiânia': {
		'country': 'brasil',
		'population': '1500000',
		'fact': 'cerrado',
		'infra': 'brt',
	},
	
	'rio claro': {
		'country': 'brasl',
		'population': '50000',
		'fact': 'interior',
		'infra': 'industries',	
	},
	
}

for city, city_info in cities.items():
	print("\nCityname: " + city.upper())
	# print(city_info.items())

	full_city = city + " " + city_info['country'] + " " + city_info['population']
	fact = city_info['fact']
	infra = city_info['infra']

	print("\tInformações da cidade: " + full_city.title())
	print("\tOs fatos e infraestrutura de cada cidade são: " + fact.title() + " " + infra.upper())

 
	
