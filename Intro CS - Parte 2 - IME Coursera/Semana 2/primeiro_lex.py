def primeiro_lex(lista):
    menor = lista[0]
    for i in lista:
        if menor > i:
            menor = i
    return menor