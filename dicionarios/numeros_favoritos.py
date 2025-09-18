numeros_favoritos = {
    'Regiane': ['996900880', '996905090'],
    'Gabriel': ['985425568', '996905544'],
    'Ilda': ['985212565', '96528589'],
    'Cassiano': ['96584515', ' 95874556'],
    'Antônio': ['985644252', ' 98564145'],
    }
    
print(numeros_favoritos['Regiane'])
print(numeros_favoritos['Gabriel'])
print(numeros_favoritos['Ilda'])
print(numeros_favoritos['Cassiano'])
print(numeros_favoritos['Antônio'])

print()

for pessoa, numero in numeros_favoritos.items():
	print("Os núḿeros favoritos de " + pessoa + " é: " + str(numero))
	

	
	
