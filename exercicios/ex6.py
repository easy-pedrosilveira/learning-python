def is_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    return texto == texto[::-1]
