# Conversão de tipos, coerção type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos: str, int, float, bool

print('a' + 'b') #concatenou

print(int('1'), type(int('1')))

# print('1' + 1) Por conta da forte tipagem do python ele não irá realizar essa função print

print(int('1') + 1) #mas dessa forma é possível

print(type(float('1') + 1)) # podendo até inserir classes 

print(bool(' ')) # aspas vazias valor é False, se tiver ao menos um espaço ele se torna True

# print(11 + 'b') # não entende se quer concatenar ou somar, retorna erro
print(str(11) + 'b')