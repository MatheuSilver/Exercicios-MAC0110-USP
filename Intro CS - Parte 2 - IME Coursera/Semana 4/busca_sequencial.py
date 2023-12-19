def busca(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return False