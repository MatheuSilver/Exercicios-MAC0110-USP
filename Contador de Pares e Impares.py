# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, 
# Determinar quantos números da sequência são pares e quantos são ímpares. Por exemplo, para a sequência
# [  6  -2  7  0  -5  8  4  ]
# O seu programa deve escrever o número 4 para o número de pares e 2 para o de ímpares.
array = input('escreva uma lista de números separados por vírgula').split(',')
impares = 0
pares = 0
for i in array:
    i = int(i)
    if i == 0:
        continue
    if i%2 == 0:
        pares += 1
    else:
       impares += 1
        
print('O número de pares é ', pares)
print('O número de impares é ', impares)
