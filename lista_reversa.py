def main():
    # escreva o seu programa abaixo e remova o print()
    separar(int(input('Insira o número de elementos')),True)
def separar(n_elementos,reverse):
    lista = []
    while n_elementos > 0:
        lista.append(float(input('Escreva um número')))
        n_elementos -= 1
        
    if reverse:
        while n_elementos < len(lista):
            n_elementos += 1
            print(lista[len(lista)-n_elementos])
    else:
        while n_elementos < len(lista):
            n_elementos += 1
            print(lista[n_elementos])
    
main()
