largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
retangulo = [list(" " * largura) for _ in range(altura)]


for j in range(0,altura):
    for i in range(0,largura):
        if (i == 0 or i == largura-1) or (j == 0 or j == altura-1):
            retangulo[j][i] = "#"
        else:
            retangulo[j][i] = " "

for j in range(0,altura):
    for i in range(0,largura):
        print(retangulo[j][i], end="")
    print()
