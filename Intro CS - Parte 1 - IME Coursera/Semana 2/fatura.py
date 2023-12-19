nome = input("Digite o nome do cliente: ")
data=(input("Digite o dia de vencimento: "))
mes=input("Digite o mês de vencimento: ")
valor=(input("Digite o valor da fatura: "))

print("Olá, %s" %nome)
print("A sua fatura com vencimento em %s de %s no valor de R$ %s está fechada." %(data, mes, valor))