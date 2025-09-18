from collections import OrderedDict

glossario = OrderedDict()

glossario['classe'] = 'Define objetos'
glossario['atributos'] = 'são características dos objetos'
glossario['métodos'] = 'ações de métodos'
glossario['função'] = 'conjunto de ações'
glossario['self'] = 'o próprio objeto'
glossario['self2'] = 'o próprio objeto'

for topico, descricao in glossario.items():
	print(topico.title() + " " + descricao.title())

'''
glossario = {
	'dicionario': 'conjunto chave valor',
    'lista': 'conjunto de infomrações',
    'variavel': 'informação armazenada',
    'instruções': 'recursos da linguagem',
    'itens': 'conteúdo de uma lista',
    }
'''

# print("O significado da palavra dicioário é: " + glossario['dicionario'].title() + ".\n")
# print("O significado da palavra lista é: " + glossario['lista'].title() + ".\n")
# print("O significado da palavra variavel é: " + glossario['variavel'].title() + ".\n")
# print("O significado da palavra instruções é: " + glossario['instruções'].title() +".\n")
# print("O significado da palavra itens é: " + glossario['itens'].title() + ".\n")

# for nome, descrição in set(glossario.items()):
	# print(nome.title() + ": " + descrição.title() + ".\n")
	
'''
glossario['classe'] = 'Define objetos'
glossario['atributos'] = 'são características dos objetos'
glossario['métodos'] = 'ações de métodos'
glossario['função'] = 'conjunto de ações'
glossario['self'] = 'o próprio objeto'
glossario['self2'] = 'o próprio objeto'

for nome,descrição in sorted(glossario.items()):
	print(nome.title() + ": " + descrição.title() + ".\n")
for nome in set(glossario.values()):
	print(nome.title())
'''


		
	
