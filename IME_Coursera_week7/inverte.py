#Mais um código antigo reaproveitado...

def main():
    # escreva o seu programa abaixo e remova o print()
    separar()

def separar():
    lista = []
    num = int(input('Escreva um número: '))
    while num != 0:
        lista.append(num)        
        num = int(input('Escreva um número: '))
        
    contador = 0
    while contador < len(lista):
        contador += 1
        print(lista[len(lista)-contador])
    
main()
