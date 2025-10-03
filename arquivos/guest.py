filename = 'guest_book.txt'

active = True
while active == True:
	nome = input("Qual o seu nome: ")
	
	if nome == 'quit':
		active = False
	
	with open(filename, 'a') as file_object:
		file_object.write(nome + "\n")
		print(nome + " Seja bem vindo")
	

