age = 85

if age < 2:
	age_msg = 'bebê'
	
elif age >= 2 and age < 4:
	age_msg = 'criança'
	
elif age >= 4 and age < 13:
	age_msg = 'garoto(a)'

elif age >= 13 and age < 20:
	age_msg = 'adolescente'

elif age >= 20 and age < 65:
	age_msg = 'adulto'
	
else:
	age_msg = 'idoso'
	
print("Essa pessoa é um " + age_msg)


