def main():
    # escreva o seu programa abaixo e remova o print()
    n_elementos = int(input('escreva o numero de elementos da sua sequencia'))
    lista = []
    while len(lista) < n_elementos:
        lista.append(float(input('Escreva um número real da sequencia')))
    lista_sem_repeticao = []
    for i in range(0, len(lista)):
        if lista[i] not in lista_sem_repeticao:
            lista_sem_repeticao.append(lista[i])
main()
#AINDA INCOMPLETO
