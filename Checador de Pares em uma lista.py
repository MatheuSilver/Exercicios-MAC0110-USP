# Dado um número inteiro n > 1 e uma sequência com n números inteiros, verificar se todos os elementos da sequência são pares

# Exemplos:
#       Para n = 5 e a sequência 24 10 6 14 74 a resposta é sim
#       Para n = 4 e a sequência 2 4 5 6 a resposta é não
Array = input('escreva uma lista de inteiros tal que o primeiro termo seja a extensão da lista').split(' ');
contador = 0;
membros = int(Array[0])
numero = 0;
while contador < membros:
    contador = contador + 1;
    numero = int(Array[contador])
    if (numero%2 != 0):
        print('Não')
        break;
    elif(contador == membros):
        print('Sim')
