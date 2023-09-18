nome = 'Pedro Neto'
altura = 1.63
peso = 71
imc = peso / (altura * altura)
# OU
imc = peso / altura ** 2

print(nome, 'tem', str(altura), 'de altura')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)