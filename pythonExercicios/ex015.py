dist = float(input('Digite quantos quilómetros foram percorridos: '))
dias = int(input('Digite quantos dias que o carro foi usado: '))

v = 60*dias + 0.15*dist

print('O valor do aluguel é: R${:.2f}'.format(v))
