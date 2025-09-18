enquete = {}

# Define uma flag para indicar que a enquete está tiva
questao_flag = True

while questao_flag:
# Pede o nome da pessoa	e o lugar do mundo
	name = input("Qual o seu nome? ")
	lugar = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
	
#Armazena as respostas no dicionário
	enquete[name] = lugar
	
# Descobre se outra pessoa vai responder à enquete
	repetição = input("Você gostaria de deixar outra pessoa responder? (sim/não) ")
	if repetição == 'não':
		questao_flag = False

# Mostra os resultados da enquete
print("\n--- Resultados ---")
for name, lugar in enquete.items():
	print(name + " gostaria de visitar " + lugar + ".")
