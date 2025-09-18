# Começa com os sanduiches que precisam ser preparados
# e com uma lista vazia para armazenar os sanduiches prontos
sandwich_orders = ['bauru', 'misto', 'pastrami', 'xtudo', 'pastrami']
finished_sandwiches = []

# Mensagem informando que a lanchonete está sem pastrami hoje
print("O lanche está sem pastrami.\n")

# Verifica cada pedido de sanduiche até o final
# Transfere os sanduiches preparados para a lista dos prontos
while sandwich_orders:
# Remove pastrami dos sandwiches
	while 'pastrami' in sandwich_orders:
		sandwich_orders.remove('pastrami')
		
	current_sandwich = sandwich_orders.pop()
	print("\tVerifying orders " + current_sandwich.title())
	finished_sandwiches.append(current_sandwich)

# Exibe todos os sandwiches preparados	
print("\nOs seguintes pedidos foram preparados: ")
for sandwich in finished_sandwiches:
	print(sandwich.title())

	
