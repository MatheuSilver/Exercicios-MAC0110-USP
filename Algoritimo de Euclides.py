# Dados dois inteiros positivos calcular o máximo divisor comum entre eles usando o algoritmo de Euclides.


numa = int(input('escreva um num'))
numb = int(input('escreva outro num'))
while numa > 0 and numb > 0:
    if numa >= numb:
        numa = numa - numb
    elif numb > numa:
        numb = numb - numa
        
if numa > 0:
    print(numa)
elif numb > 0:
    print(numb)
    
# pequena nota sobre o algoritmo de euclides, em resumo, o MDC pode ser calculado subtraindo o menor número do maior em dado par até o ponto em que algum dos dois seja ZERO
# Mais informações do Algoritmo, consultar: https://pt.wikipedia.org/wiki/Algoritmo_de_Euclides
