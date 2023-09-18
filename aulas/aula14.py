# Função format (método)

# string = 'a={1} b={0} c{2:.2f}'  mexer pelos indices

# Parametro nomeado
# formato = string.format(a,b,nome3=c)
# A e B são argumentos já o C é um parametro

a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c{nome3:.2f}' 
formato = string.format(nome1=a, nome2=b,nome3=c)

print(formato)