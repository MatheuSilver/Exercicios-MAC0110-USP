# Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.
n = int(input('escreva um número'))
k = int(input('escreva o expoente desse numero'))
potencia = int(n)
while k > 1:
    potencia = potencia*n
    k=k-1
print(potencia)
