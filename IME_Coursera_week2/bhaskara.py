import math

# Recebe os coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica o número de raízes reais e imprime o resultado
if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    # Raiz única (ou raiz dupla)
    raiz = -b / (2*a)
    print(f"a raiz{' dupla' if delta == 0 else ''} desta equação é {raiz}")
else:
    # Duas raízes reais distintas
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"as raízes da equação são {min(raiz1, raiz2)} e {max(raiz1, raiz2)}")
