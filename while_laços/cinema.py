prompt = "\nQual a sua idade? "
prompt += "digite 'quit' para interromper o aplicativo!"

active = True
while active:
	idade = input(prompt)
	
#	if idade == 'quit':
#		active = False
		
	if idade == 'quit':
		break
		
	elif int(idade) < 3:
		print("\nO valor do seu ingresso é gratuíto para entrar no cinema")
		
	elif int(idade) >= 3 and int(idade) <= 12:
		print("\nO valor do seu ingresso é de R$ 10,00 para entrar no cinema")
	
	elif int(idade) > 12:
		print("\nO valor do seu ingresso é de R$ 12,00 para entrar no cinema")
		
	else:
		print("\nEsse valor não corresponde a uma idade válida!")
		
	
