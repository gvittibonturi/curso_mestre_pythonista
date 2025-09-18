#Desafio da Aula usar o datatime para saber quantos dias faltam para o meu aniversário.
#dados de entrada: dia do aniversário
#ressultado esperado a diferença entre o a data atual comm a data do proximo aniversário
from datetime import datetime
dt_atual = datetime.now()
dt_prox_niver = datetime.strptime(input('Qual a data do teu próximo aniversário :  '),'%d/%m/%Y')
meses_faltam = (dt_prox_niver).month
dias_faltam = (dt_prox_niver - dt_atual).days
dias_falta_resto = dias_faltam % meses_faltam
#print(f'Rapa, ainda faltam {} dias para o teu proxímo aniversário. Mas, parabéns desde já!')
print(dias_falta_resto)
if dias_faltam < 31 :
    print(f'Rapa, ainda faltam {dias_faltam} dias para o teu proxímo aniversário. Mas, parabéns desde já!')
else:
    print(f'Rapa, ainda faltam {meses_faltam} meses e {dias_falta_resto} para o teu proxímo aniversário. Mas, parabéns desde já!')