# Dado um número inteiro n >= 0, calcular n!.
fatorial = int(input('Escreva um número pra tirar seu fatorial'))
maior = fatorial
while maior > 1:
    maior = maior - 1
    fatorial = fatorial*(maior)
print(fatorial)
