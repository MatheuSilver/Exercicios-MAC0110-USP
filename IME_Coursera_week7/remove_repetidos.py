def remove_repetidos(lista):
    sem_repeticoes = []
    for i in lista:
        if i not in sem_repeticoes:
            sem_repeticoes.append(i)
    return sorted(sem_repeticoes)