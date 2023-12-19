def maior_primo(x): #Só reaproveitando mesmo k
    contador = 1
    while contador < x:
        contador += 1
        if contador == x:
            return x
        elif (x%contador == 0):
            return maior_primo(x-1)
        

def n_primos(x):
    contador = maior_primo(x)
    num_primos=1
    while contador > 2:
        contador = maior_primo(contador-1)
        num_primos+=1
    return num_primos