# Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
quantidade = int(input('escreva a quantidade de números a serem carregados'))
n = int(input('escreva um número'))
j = int(input('escreva outro num'))
leNums = 0;
while quantidade > 0:
    if leNums%n == 0 or leNums%j == 0:
        print(leNums)
        quantidade = quantidade - 1
    leNums = leNums + 1
        
print('aqui cabo')
