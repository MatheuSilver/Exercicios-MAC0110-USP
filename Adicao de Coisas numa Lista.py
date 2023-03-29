# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, determinar a soma dos pares. Por exemplo, para a sequência
# Resumindo a explicação da questão: o primeiro elemento da lista deve ser o quão longe vamos ir na array, e o resto, são os elementos a serem checados.
# a parte do divisor custom não era nescessáriamente pra ser custom k
# E ainda sobre isso, segundo o exemplo de output dado, para uma array [ 6 2 7 0 5 8 ], tal que queremos somar apenas pares ou seja n = 2, o resultado esperado é 14
n = int(input('escreva um divisor ai meu bom'))
sequencia = input('Escreva uma sequencia ai meu nóbrega').split(',')
leSoma = 0
contador = -1
i = 0
while contador < int(sequencia[0]):
    contador += 1
    if contador == 0:
        continue
    i = int(sequencia[contador])
    if i%n == 0:
        leSoma += i
print(leSoma)
