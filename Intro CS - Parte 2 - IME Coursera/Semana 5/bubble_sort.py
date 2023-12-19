def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista


#Modificações:
#Agora ele percorre a lista do começo ao fim e imprime o estado da array a cada interação.