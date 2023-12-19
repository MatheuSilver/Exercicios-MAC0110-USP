import random

class Algoritmos:
    ###-----------------ALGORITMOS DE BUSCA-----------------###

    def busca_sequencial(lista, x):
        '''
        Dada uma lista qualquer, a função percorre cada elemento indo de 0 até o fim da lista
        procurando por este elemento.
        Caso ele não seja encontrado a função devolve False
        Caso contrário, devolve True
        '''
        for i in range(len(lista)):
            if lista[i] == x:
                return True
        return False
    


    '''
    O algoritmo abaixo funciona da forma:

        1. Ele determina quem são os extremos da função
        2. Em seguida, ele calcula o ponto médio entre esses extremos
        3. Caso esse elemento seja o procurado, então ele para a busca
            3.1 Caso o elemento seja maior do que o de dada posição, então
                ele altera o limite inferior para o ponto atual + 1
                (sugestão: experimente tirar esse + 1 pra ver o que acontece : D )
            3.2 Caso o elemento seja menor, então o limite inferior
                passará a ter o valor da média.

        4. Se em algum momento, o ponto1 e o ponto2 convergirem
            Isso significaria que a lista inteira foi percorrida
            se nessa última verificação o elemento em ponto1 = ponto2
            não for igual ao procurado, entao este elemento não existe na lista.
         
    '''
    def busca_binaria(lista, x):
        '''
        Certifique-se de que a lista fora ordenada antes de usar este algoritmo.
        Verifica no pior dos casos um total de "funcao_piso(len(lista)/4)" vezes a lista em busca do numero desejado
        Se ele é encontrado retorna True, caso contrário, retorna False.
        '''
        ponto1 = len(lista)
        ponto2 = 0
        while ponto1 != ponto2:
            pb = (ponto1 + ponto2) // 2
            if lista[pb] == x:
                return True
            elif lista[pb] > x:
                ponto1 = pb - 1
            else:
                ponto2 = pb + 1
        return False
                
    ###---------------ALGORITMOS DE ORDENAÇÃO---------------###

    '''
    O algoritmo abaixo funciona da forma:
        1. Ele determina uma posição não verificada inicial
        2. Com essa posição, ele verifica se o dado em outras posições posteriores é maior do que o da posição de analise
        3. Caso encontre alguem, então ele irá atualizar a "menor posição" e continuará a verificação
        4. Caso não encontre ninguem, então ele irá trocar o elemento da posição inicial de análise (supostamente o menor) com o da real menor posição.
        5. Por fim, ele avança a próxima posição não verificada e percorre a lista inteira de novo fazendo o mesmo processo.
    '''
    
    def selecao_direta(lista):
        '''
        Dada uma lista qualquer, a função irá ordenar de forma crescente os conteudos desta lista
        e no final, irá devolver esta lista ordenada.
        '''
        fim = len(lista)
        for i in range(fim -1):
            min_pos = i
            for j in range(i+1, fim):
                if lista[j] < lista[min_pos]:
                    min_pos=j
            lista[i], lista[min_pos]=lista[min_pos],lista[i]
        return lista
    
    '''
    O algoritmo abaixo funciona da forma:
        1. Assuma que o primeiro elemento da lista já está ordenado.
        2. Assuma também que os elementos a frente deste não estão ordenados
        3. Do primeiro elemento não ordenado, verifica a porção ordenada por inteiro
           de trás pra frente pra saber se ele deve empurrar alguem pra frente.
                Exemplo:
                    Se o elemento na posição 10 for menor que o elemento na posição 9
                    Então os dois trocam de lugar, ou (o 10 empurra o 9 pra posição 10)
                    E o elemento que estava em 10 agora ocupará a posição 9.
                    esse processo irá se repetir até que o elemento seja menor do que o seu sucessor (de trás pra frente)
    '''
    
    def insercao_direta(lista):
        '''
        Dada uma lista qualquer, a função irá ordenar de forma crescente os conteudos desta lista
        e no final, irá devolver esta lista ordenada.
        '''
        for i in range(1,len(lista)):
            for j in range(i-1, -1, -1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista
    
    '''
    Este é bem parecido com o anterior, então vou resumir um pouquinho com a analogia do tubo de ensaio.

    O algoritmo abaixo funciona da forma:
        1. Tome o último elemento de uma lista
        2. Então, percorre todos os elementos da lista, verificando se, o elemento na posição atual
           é maior que o da posição a sua frente, isto é se o elemento em 9 é maior que o elemento em 10
        3. Se ele encontrar alguem com a descrição de 2) então ele troca ambos de lugar e assim vai indo 
           até este chegar ao começo da lista. (lembre-se que partimos do final)

    Segundo a analogia do tubo de ensaio.
        Seria meio que, pegamos o elemento no topo (fim da lista), e arrastamos ele pra baixo conforme
        sua densidade (ou tamanho) até encontramos alguém mais pesado que ele.
    '''
    
    def bubble_sort(lista):
        '''
        Dada uma lista qualquer, a função irá ordenar de forma crescente os conteudos desta lista
        e no final, irá devolver esta lista ordenada.
        '''
        for i in range(len(lista)-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]: #Se trocar o > por < então passa a ser na forma decrescente.
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista
    #Um pequeno adendo no bubble sort na prova: "Algoritmo de Ordenação da Bolha e Testes Automatizados"
    #A resposta correta para a pergunta (Verifique isso com o código) deveria ser [2, 5, 1, 3, 4]
    #Mas o corretor do coursera assume que a resposta correta é [2, 1, 3, 4, 5]
    
    #Isso é até possível teóricamente, se o bubble sort ocorresse indo do começo ao fim
    #Entretanto, ele ordena percorrendo a lista do fim ao começo assim como informado na função acima.
    
if __name__ == "__main__":
    tamanho_lista = 10
    maior_elemento = 30
    numeros_aleatorios = [random.randint(0, maior_elemento) for _ in range(tamanho_lista)]
    #Copiei a parte de cima ai do chat gpt mesmo k
    #Preguiça de pensar em algo pra gerar numero aleatório pra teste.

    print(Algoritmos.bubble_sort(numeros_aleatorios))