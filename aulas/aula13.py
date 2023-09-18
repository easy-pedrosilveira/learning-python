# FORMATAÇÃO = f strings

nome = 'Pedro Neto'
altura = 1.90
peso = 71
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1, '\n', linha_2, '\n', linha_3  )