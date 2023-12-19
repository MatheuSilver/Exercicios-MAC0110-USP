import random

def lista_grande(n):
    lista = list(range(n)) #Não tenho certeza se havia algum método primitivo para fazer isso...
    random.shuffle(lista)
    return lista