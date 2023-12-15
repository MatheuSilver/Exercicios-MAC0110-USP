secs = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = secs // (24 * 3600)
horas = (secs % (24 * 3600)) // 3600
minutos = (secs % 3600) // 60
segundos = secs % 60
print("%i dias, %i horas, %i minutos e %i segundos." % (dias, horas, minutos, segundos))