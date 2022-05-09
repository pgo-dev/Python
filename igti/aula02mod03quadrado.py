lado = int(input('Números de lados: '))

for l in range(0, lado):
    for c in range(0, lado):
        print('O ' if (l+c) % 2 == 0 else 'X ', end='')
    print('')



