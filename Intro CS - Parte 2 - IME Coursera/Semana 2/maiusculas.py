def maiusculas(frase):
    f = ""
    for i in frase:
        if ord(i)>=65 and ord(i)<=90:
            f+=i
    return f