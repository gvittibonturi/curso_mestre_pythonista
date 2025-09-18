prompt = "\nQual ingrediente você gostaria de adicionar na pizza:"
prompt += "\nDigite 'quit' para interromper o programa. "

message = ""
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		print("Você adicionou o ingrediente " + message + " em sua pizza!")
	
