def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

num = int(input("Digite um número inteiro não negativo: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é {resultado}")
