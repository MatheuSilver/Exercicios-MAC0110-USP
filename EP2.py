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
  Turma: 52
  Prof.: Renata Wassermann

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

'''
Referências:
Tanto a função seno quanto cosseno foram reaproveitadas de soluções desenvolvidas por mim mesmo
para as listas de exercícios disponíveis em:
https://panda.ime.usp.br/panda/static/cc110/

Cujo link também é referenciado no material didático da disciplina.
'''

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

GRAVIDADE = 9.81
EPSILON = 0.01
DELTA_T = 0.01
PI = 3.14159265358979323846

#Constante definindo precisão de dez casas decimais onde é pedido.
PRECISAO = 10 

def fatorial(num):
    '''
    Recebe um numero e devolve o fatorial dele.
    '''
    resultado = 1
    while num > 0:
        resultado = resultado*num
        num -= 1
    return (resultado)

def grad_para_rad(theta):
    '''
    Converte um dado angulo de graus para radianos.
    '''
    return theta*PI/180

def abs(num):
    '''
    Recebe um número qualquer e retorna o módulo dele.
    Só fiz minha própria versão pra não precisar nescessariamente
    usar algum import.
    '''
    if num < 0:
        num *= -1
    return num


def seno(theta):
    '''
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    '''
    #Correção requirida pelo avaliador automático.
    theta = grad_para_rad(theta)
    somatorio = 0
    potencia = 1
    contador = 2
    prevSomatorio = 1
    while abs(prevSomatorio - somatorio) > 10**-PRECISAO:
        prevSomatorio = somatorio
        somatorio += ((-1)**contador)*(theta**potencia)/fatorial(potencia)
        contador += 1
        potencia +=2
    return somatorio

def cosseno(theta):
    '''
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    '''
    #Correção requirida pelo avaliador automático.
    theta = grad_para_rad(theta)
    somatorio = 0
    potencia = 0
    contador = 2
    prevSomatorio = 1
    while abs(prevSomatorio - somatorio) > 10**-PRECISAO:
        prevSomatorio = somatorio
        somatorio += ((-1)**contador)*(theta**potencia)/fatorial(potencia)
        contador += 1
        potencia +=2
    return somatorio


def raizQuadrada(x):
    '''
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    '''
    a = x
    b = 1/2*(a+x/a)
    while abs(a - b) > 10**-PRECISAO:
        a = b
        b = 1/2*(a+x/a)
    return b

def distanciaPontos(x1, y1, x2, y2):
    '''
    Esta função calcula a distância entre dois pontos dados por
    (x1, y1) e (x2, y2).
    Entrada: As coordenadas de dois pontos no plano, x1, y1, x2, y2,
    em metros.
    Saída: A distância entre (x1, y1) e (x2, y2) em metros.
    '''
    return (raizQuadrada((x1-x2)**2+(y1-y2)**2))

def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    return (x + vx*dt, y + vy*dt - (GRAVIDADE*dt**2)/2)


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    return(vx, vy - GRAVIDADE*dt)


'''
Importante notar para o caso da aproximação de um círculo que
caso a distancia entre o pokemon e a pokebola seja menor que r
isso quer dizer que a pokebola está no raio de alcance.
'''
def houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r):
    '''
    Esta função calcula se houve ou não colisão entre a pokebola e o
    pokemon considerando-se um raio r.
    Entrada: posição x e y da pokebola, posição x e y do pokemon
    e o raio r, todas medidas em metros.
    Saída: Retorna True caso haja colisão, e False caso contrário.
    '''
    return (distanciaPontos(xpokebola,ypokebola,xpokemon,ypokemon)) <= r

def simula_lancamento (xpokebola, ypokebola,
                       vlancamento, angulolancamento,
                       xpokemon, ypokemon, r):
    '''
    Esta função simula o lançamento da bola até que ela atinja o
    pokemon, ou o solo a menos de EPSILON.
    Na simulação, considere as seguintes constantes:
    EPSILON é uma constante de precisão de 1.0e-2 metro.
    DELTAT é uma constante de precisão de 1.0e-2 segundo.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola)
    em metros.
    Posição do pokemon (xpokemon e ypokemon) em metros.
    Velocidade escalar em metros por segundo
    e ângulo de lançamento em graus.
    O raio r em metros.
    Saída: Três valores: Um booleano (True se o lançamento teve sucesso 
    e acertou o pokemon, ou False caso contrário) e as coordenadas finais
    x e y da pokébola.
    '''
    acertou = False
    velocidades = [vlancamento*cosseno(angulolancamento), vlancamento*seno(angulolancamento)]
    data = [xpokebola, ypokebola]
    while data[1] > EPSILON and not acertou:
        if (houveColisao(data[0], data[1], xpokemon, ypokemon, r)):
            acertou = True
        else:
            data = atualizaPosicao(data[0], data[1], velocidades[0], velocidades[1])
            velocidades = atualizaVelocidade(velocidades[0], velocidades[1]) #Só pra não precisar rodar isso duas vezes.
            
    return (acertou, data[0], data[1])

def main():
    tentativas = 1
    xp = float(input("Digite a coordenada x do pokemon: "))
    yp = float(input("Digite a coordenada y do pokemon: "))
    r  = float(input("Digite o raio do pokemon (> 0) em metros: "))
    acerto = False
    while tentativas < 4 and not acerto:
        print('Tentativa ', tentativas)
        xb = float(input('  Digite a coordenada x do treinador: '))
        yb = float(input('  Digite a coordenada y do treinador: '))
        velocidade = float(input('  Digite a velocidade de lancamento em m/s: '))
        #Honestamente eu preferiria usar conforme abaixo que a função só é aplicada uma vez por tentativa, mas devido ao requerimento do avaliador automático.
        #Tal função de conversão foi movida diretamente para dentro das funções seno e cosseno.
        
        #angulo = grad_para_rad(float(input('  Digite o angulo de lancamento em graus: ')))
        
        angulo = float(input('  Digite o angulo de lancamento em graus: '))
        data = simula_lancamento(xb, yb, velocidade, angulo, xp, yp, r)
        
        tentativas += 1
        acerto = data[0]

        if acerto:
            print('A pokebola atingiu o pokemon.')
        else:
            print('A pokebola nao atingiu o pokemon por %.4f metros.' %(distanciaPontos(data[1],data[2], xp, yp)))



# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================



# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================
