def menor_nome(nomes):
    menor = nomes[0].strip().capitalize()
    for i in range(len(nomes)):
        nome = str(nomes[i]).strip().capitalize()
        if len(menor) > len(nome):
            menor = nome
    return menor