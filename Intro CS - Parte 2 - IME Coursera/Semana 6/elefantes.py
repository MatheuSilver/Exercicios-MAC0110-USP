def elefantes(n):
    if n <= 1:
        return ""
    elif n == 2:
        return "Um elefante incomoda muita gente\n2 elefantes " + incomodam(2) + "muito mais"
    else:
        frase_anterior = elefantes(n - 1)
        return (
            frase_anterior + f"\n{n-1} elefantes incomodam muita gente\n{n} elefantes "
            + incomodam(n) + "muito mais"
        )

def incomodam(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n - 1)
    
    ##INCOMODA MUITO TÉ DOIDO...
