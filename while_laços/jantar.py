prompt = "Quantas pessoas estão com você? "
prompt += "\nNa verdade, quantas irão jantar? "

qtd_pessoas = input(prompt)

qtd_pessoas = int(qtd_pessoas)

if qtd_pessoas > 8:
	print("\nEsperem uma mesa para " + str(qtd_pessoas) + " pessoas ser liberado, por gentileza")
else:
	print("\nA mesa de vocês já está pronta!")


