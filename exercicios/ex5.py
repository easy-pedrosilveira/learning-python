def encontrar_segundo_maior(lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[1]
