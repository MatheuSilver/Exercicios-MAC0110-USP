def insertion_sort(lista): #Zero modificações de algoritmos.py
    for i in range(1,len(lista)):
        for j in range(i-1, -1, -1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista