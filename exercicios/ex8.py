def contar_vogais(texto):
    vogais = "AEIOUaeiou"
    count = 0
    for char in texto:
        if char in vogais:
            count += 1
    return count
