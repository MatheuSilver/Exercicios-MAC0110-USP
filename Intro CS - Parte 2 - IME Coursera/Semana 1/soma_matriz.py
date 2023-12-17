def soma_matrizes(m1, m2):
    if (len(m1)+len(m1[0])!=len(m2)+len(m2[0])):
        return False
    else:
        matriz_somada = []
        for i in range(len(m1)):
            linha = [0]*len(m1[0])
            for j in range(len(m1[0])):
                linha[j] = m1[i][j]+m2[i][j]
            matriz_somada.append(linha)
        return matriz_somada