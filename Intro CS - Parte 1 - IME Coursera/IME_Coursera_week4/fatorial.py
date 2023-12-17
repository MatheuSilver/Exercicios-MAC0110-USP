# Dado um número inteiro n >= 0, calcular n!.
fatorial = int(input('Digite o valor de n: '))
if (fatorial==0):
    print(1)
else:
    maior = fatorial
    while maior > 1:
        maior = maior - 1
        fatorial = fatorial*(maior)
    print(fatorial)
