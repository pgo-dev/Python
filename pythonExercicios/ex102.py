def fat(n, show=False):
    f = 1
    if show:
        for c in range(n, 1, -1):
            f = f * c
            print(f'{c} x ', end='')
        print(f'1 = {f}')
    else:
        for c in range(n, 0, -1):
            f = f * c
        print(f)

n = int(input('N: '))
mostrar = str(input('Show? [s/n] ')).strip().lower()

if mostrar == 's':
    mostrar = True
elif mostrar == 'n':
    mostrar = False

fat(n, mostrar)
