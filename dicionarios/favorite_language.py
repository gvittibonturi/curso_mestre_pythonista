favorite_language = {
	'jen': 'python',
	'sarah': 'C',
	'eduard': 'ruby',
	'phil': 'python',
	'paulo': 'java',
	'antônio': 'R',
	}
	
for name, language in favorite_language.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")
		
print("\n\n")
	
	
enquete = ['antônio', 'paulo', 'gustavo', 'sarah']


for enquete_name in enquete:
	
	if enquete_name in favorite_language:
		 print("Obrigado " + enquete_name.title() + " por participar da enquete!")
	else:
		print("Por favor " + enquete_name.title() + " responda à esquete.")
		

	
