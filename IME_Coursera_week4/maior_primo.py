def maior_primo(x):
    contador = 1
    while contador < x:
        contador += 1
        if contador == x: #Obviamente tem como melhorar esse algoritmo, mas preguiça
            return x
        elif (x%contador == 0):
            return maior_primo(x-1)