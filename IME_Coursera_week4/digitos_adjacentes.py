# Dado um número inteiro n > 1, verificar se n tem dois dígitos adjacentes iguais.

# exemplos
# Para n = 21212 a resposta é não
# Para n = 212212 a resposta é sim

# Esta foi a primeira tentativa de solução, entretanto existe uma outra melhor pensada logo depois dessa
# Que usa coisas menos complexas, cujo o arquivo possui o mesmo nome que este.
n = int(input("Digite um número inteiro: "));
prevnum = n%10
n//=10
achou = False
while (n > 0 and not achou):
    next_num=n%10
    if prevnum==next_num:
        achou = True
        print("sim")
    prevnum=next_num
    n//=10
if not achou:
    print("não")

