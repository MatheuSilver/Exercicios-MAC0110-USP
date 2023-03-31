# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, verificar se a sequência é uma progressão aritmética.
# Isso seria muito mais fácil de fazer com arrays, mas ao mesmo tempo tambem seria muita apelação...

# Basicamente recebe a quantade de termos que irá existir na progressão
quantidade = int(input('Insira a quantidade de elementos a serem avaliados'))-1

# Recebe o primeiro elemento e o segundo
primeironum = int(input('Insira o primeiro número da sequência'))
posnum = int(input('Insira o segundo número da sequência'))

#Razão da progressão
razao = posnum - primeironum
contador = 2;
# Caso o número de elementos seja menor ou igual a 2, não irá ir pro while e irá retornar ao usuário que não tem como fazer sequência com poucos elementos.
if contador > quantidade:
    print('Quantidade de termos insuficiente')
    
# O segundo check do while serve para o check parar logo que identificar uma incosistência na sequência aritmética
while contador <= quantidade and primeironum == posnum - razao*(contador-1):
    
    # Contador sobe logo de cara pra garantir que o R da progressão se desloque para o próximo termo antes dos checks
    contador += 1;
    
    # Neste ponto, pos num equivale ao terceiro termo em diante da sequência
    posnum = int(input('Insira outro número'))
    
    # contador > quantidade quer dizer que a sequência chegou ao fim, e portanto se ela rodou até aqui, é porque a sequência é aritmética
    if(contador > quantidade and primeironum == posnum - razao*(contador-1)):
        print('É uma Sequência Aritmética')
        
        
    if (primeironum != posnum - razao*(contador-1)):
        print('Não é uma sequência Aritmética')
    
