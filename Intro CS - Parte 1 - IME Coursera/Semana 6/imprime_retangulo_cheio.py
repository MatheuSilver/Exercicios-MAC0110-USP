largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
retangulo = [[0]*largura]*altura

for j in range(0,altura):
    for i in range(0,largura):
        retangulo[j][i] = "#"

for j in range(0,altura):
    for i in range(0,largura):
        print(retangulo[j][i], end="")
    print()
