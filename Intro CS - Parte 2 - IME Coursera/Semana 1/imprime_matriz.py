#Obviamente essa função NUNCA foi usada em NENHUM EP do IME...
#Principalmente EP's que envolvam pokemons ou coisa do genero...
#Fonte: Confia : D

def imprime_matriz(matriz):
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    for i in range(len(matriz)):
        linha = ''
        for j in range(len(matriz[i])):
            linha += str(matriz[i][j])
            if j != (len(matriz[i])-1):
                linha += " "
        print(linha)