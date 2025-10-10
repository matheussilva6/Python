segundostotal = int(input("Insira os segundos para deixar em horas, minutos e segundos: "))

horas = segundostotal // 3600
minutos = (segundostotal % 3600) // 60
segundosrestantes = segundostotal % 60

print(horas, "horas,", minutos, "minutos e", segundosrestantes, "segundos")