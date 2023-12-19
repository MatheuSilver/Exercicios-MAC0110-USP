def ordena(lista): #Também copiado de Algoritmos.py
    fim = len(lista)
    for i in range(fim -1):
        min_pos = i
        for j in range(i+1, fim):
            if lista[j] < lista[min_pos]:
                min_pos=j
        lista[i], lista[min_pos]=lista[min_pos],lista[i]
    return lista