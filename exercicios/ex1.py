segundos = input("insira os segundos para deixar em horas, minutos e segundos")
horas = segundos //3600
minutos = (segundos % 3600) // 60
segundo_restante = segundos % 60
print (horas"horas: ", minutos)
