import json

filename = 'num_favorito.json'

with open(filename) as f_obj:
	num_favorito = json.load(f_obj)
	

print("Eu sei qual é o seu número favorito! É " + num_favorito + ".")

