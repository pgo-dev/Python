g = list()
dados = list()
leves = pesadas = n = cont = 0

while True:

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    g.append(dados[:])
    dados.clear()

    n = n + 1

    if cont == 0:
        leves = pesadas = g[0][1]

    if cont >= 1:
        if g[cont][1] >= pesadas:
            pesadas = g[cont][1]

        elif g[cont][1] <= leves:
            leves = g[cont][1]

    cont = cont + 1

    conf = str(input('Deseja continuar: [s/n] '))
    if conf == 'n':
        break

print(f'Foram cadastradas {n} pessoas.\n')

print(f'O maior peso foi de {pesadas} kg. Peso de: ', end='')
for c in range(0, len(g)):
    if g[c][1] == pesadas:
        print(g[c][0], end=' ')

print(f'\nO menor peso foi de {leves} kg. Peso de: ', end='')
for c in range(0, len(g)):
    if g[c][1] == leves:
        print(g[c][0], end=' ')