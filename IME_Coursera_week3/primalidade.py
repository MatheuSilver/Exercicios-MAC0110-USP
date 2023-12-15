# Dado um número inteiro n > 1, verificar se n é primo.
# Honestamente, tenho minhas dúvidas de até que ponto isso aqui é viável, mas whatever, isso funciona omega kek
primo = int(input('Digite um número inteiro: '));
contador = 1;
while contador < primo:
    contador += 1;
    if(contador == primo):
        print('É primo!');
        break
    elif (primo%contador == 0):
        print('Não é primo!');
        break;
