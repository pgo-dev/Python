import datetime

print(datetime.datetime.now())

h = int(datetime.datetime.now().hour)
m = int(datetime.datetime.now().minute)
s = int(datetime.datetime.now().second)

print(f'Faltam {24 - h} horas, {60 - m} minutos e {60 - s} segundos para terminar o dia')

t = [12, 10]
ti = [int(((h * 60 + m - t[1]) / 60)-t[0]), (h * 60 + m - t[1]) % 60]

print(f'This stream started at {ti[0]}:{ti[1]}')
