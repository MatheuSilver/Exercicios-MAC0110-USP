def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    soma = lista[len(lista)-1]
    lista.pop()

    return soma+soma_lista(lista)