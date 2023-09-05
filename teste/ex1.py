N = int(input("Digite um número: "))
soma = 0

for i in range(2, N + 1, 2):
    soma += i

print(f"A soma dos números pares de 1 a {N} é {soma}")