rios = {
	'nilo': 'egito',
	'são francisco': 'brasil',
	'senna': 'frança'
	}
	
for rio,país in rios.items():
	print("O " + rio.title() + " corre pelo " + país.title())

print("\n")
	
for rio in rios.keys():
	print(rio.title())
	
print("\n")

for país in rios.values():	# percorre os valores do dicionário
	print(país.title())
