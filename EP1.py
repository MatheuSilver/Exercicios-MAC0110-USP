"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Matheus Silveira Feitosa
  NUSP : 11836692
  Turma: 51
  Prof.: Renata Wassermann

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""


# Escreva o seu código aqui :-)
pokebolasNUM = int(input(' Digite o numero N de pokebolas:\n'))

#Dados da Região e do Pokemon
g = int(input('Digite o valor da gravidade:\n'))
xp = int(input('Digite a coordenada x (inteiro >= 0) do pokemon:\n'))
yp = int(input('Digite a coordenada y (inteiro >= 0) do pokemon:\n'))

#Utilidades para retorno e controle de loop
tentativas = 0
bateu = False

#Inicialização de Variáveis da Pokebola feita com relação a posição do pokemon
#Só pra garantir a inicialização sem correr o risco de a pokebola já iniciar na posição do pokemon
#E então poder entrar no looping
xb = xp - 1
yb = yp - 1

while pokebolasNUM > 0 and not bateu:
    #Basicamente essa primeira parte do loop deverá servir apenas para permitir que novas variáveis sejam escolhidas
    pokebolasNUM -= 1
    tentativas += 1
    
    print('\nTentativa ', tentativas, ':\n')
    xt = int(input('Digite a coordenada x (inteiro >= 0) do treinador:\n'))
    yt = int(input('Digite a coordenada y (inteiro >= 0) do treinador:\n'))
    vyli = int(input('Digite a componente y da velocidade de lancamento:\n'))
    
    #Inicialização das variáveis da Pokebola.
    xb = xt
    yb = yt
    
    tempo = 0
    
    #Esse ultimo aqui é só pra caso em algum momento, queiramos fazer a velocidade vx de lançamento ser variável.
    vxl = 1 #int(input('Insira a velocidade de lançamento da pokebola no eixo X'))
    
    
    while (yb > 0 and xb < xp) or tempo == 0:
        xb = xt+vxl*tempo
        yb = yt+vyli*tempo-g/2*tempo*tempo
        
        #Os int's colocados aqui, foram apenas para garantir que o resultado entregue ao usuário
        #Seja um número inteiro independente das variáveis escolhidas.
        print('> t=   ', int(tempo), '    vy=   ', int(vyli-g*tempo), '    x=   ', int(xb), '    y=  ', int(yb))
        
        tempo += 1
        
        if(xp==xb and yp==yb):
            bateu = True
        
        

    if(bateu):
       print('A pokebola atingiu o pokemon.')
    else:
        print('A pokebola nao atingiu o pokemon.')