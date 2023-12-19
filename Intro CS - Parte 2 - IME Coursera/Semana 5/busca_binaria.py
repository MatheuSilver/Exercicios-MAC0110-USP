def busca(lista, x):
    ponto1 = len(lista) - 1
    ponto2 = 0

    while ponto1 >= ponto2:
        pb = (ponto1 + ponto2) // 2
        print(pb)

        if lista[pb] == x:
            return pb
        elif lista[pb] > x:
            ponto1 = pb - 1 
        else:
            ponto2 = pb + 1

    return False


#Modificações feitas de algoritmos.py:
#Agora ele retorna o indice, imprime o pb a cada interação (e fim dela)

#Foi mais díficil fazer o testador imprimir o que o coiso queria
#Do que propriamente fazer o algoritmo funcionar k