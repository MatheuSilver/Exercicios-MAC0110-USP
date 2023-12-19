def ordenada(lista):
    for i in range(1,len(lista)):
        if lista[i-1] > lista[i]:
            return False
    return True