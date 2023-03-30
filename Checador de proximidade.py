# Dado um número inteiro n > 1, verificar se n tem dois dígitos adjacentes iguais.

# exemplos
# Para n = 21212 a resposta é não
# Para n = 212212 a resposta é sim

# Esta foi a primeira tentativa de solução, entretanto existe uma outra melhor pensada logo depois dessa
# Que usa coisas menos complexas, cujo o arquivo possui o mesmo nome que este.
n = int(input("Escreva uma sequência de números"));
array = []
divisoes = 0;
while n != 0:
    array.append(n%10);
    n = int(n/10);
    divisoes += 1;
contador = 0;
while contador < divisoes:
    if(int(array[contador]) == int(array[contador + 1])):
        print('Sim');
        break;
    elif(contador == divisoes-2):
        print('Não')
    contador +=1
