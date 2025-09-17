current_users = ['Glauco', 'Antonio', 'Silvia', 'Pamela', 'Alda']

new_users = ['Marcelo', 'GLAUCO', 'Regiane', 'Tiago', 'Antonio']
#new_users = []

if new_users:
	for new_user in new_users:
		nome_novo_minusculo = new_user
		nome_corrente_minusculo = new_users
		if nome_novo_minusculo in nome_corrente_minusculo:
			print("O usuário " + nome_novo_minusculo.title() + " deverá fornecer um novo nome para cadastro")
		else:
			print("O nome " + nome_novo_minusculo.title() + " pode ser cadastrado como novo usuário")
else:
	print("Lista vazia")
	