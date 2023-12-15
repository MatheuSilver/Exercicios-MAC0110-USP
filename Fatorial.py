# Dado um número inteiro n >= 0, calcular n!.
fatorial = int(input('Digite o valor de n: '))
maior = fatorial
while maior > 1:
    maior = maior - 1
    fatorial = fatorial*(maior)
print(fatorial)
