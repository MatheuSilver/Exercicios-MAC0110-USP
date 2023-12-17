def conta_letras(frase, contar="vogais"):
    vogais = 0
    frase = frase.lower().strip().replace(" ", "")
    for letra in frase:
        if letra == "a" or letra == "e" or letra == "i" or letra=="o" or letra == "u":
            vogais+=1
    if contar != "vogais":
        return len(frase)-vogais
    else:
        return vogais