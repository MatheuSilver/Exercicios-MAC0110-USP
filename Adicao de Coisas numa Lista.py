# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, determinar a soma dos pares. Por exemplo, para a sequência
# Resumindo a explicação da questão: o primeiro elemento da lista deve ser o quão longe vamos ir na array, e o resto, são os elementos a serem checados.
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
