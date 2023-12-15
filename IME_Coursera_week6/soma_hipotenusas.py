def é_hipotenusa(n2):
    for i in range(1, n2):
        for j in range(1, n2):
            if i**2 + j**2 == n2**2:
                return True
    return False

def soma_hipotenusas(n1):
    soma = 0
    for num in range(1, n1 + 1):
        if é_hipotenusa(num):
            soma += num
    return soma
