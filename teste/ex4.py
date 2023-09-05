def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

num = int(input("Digite um número inteiro: "))
resultado = soma_digitos(num)
print(f"A soma dos dígitos de {num} é {resultado}")
