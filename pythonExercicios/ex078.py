l = list()

for c in range(0, 5):
    l.append(int(input(f'Digite o {c + 1}º valor da lista: ')))

posmaior = list()
posmenor = list()

for c in range(0, len(l)):
    if l[c] >= max(l):
        posmaior.append(c)

    if l[c] <= min(l):
        posmenor.append(c)

if len(posmaior) > 1:
    print(f'O maior valor é {max(l)} e aparece nas posições ', end='')
    for c in range(0, len(posmaior)):
        print(f'{posmaior[c]}... ', end='')

if len(posmaior) == 1:
    print(f'O maior valor é {max(l)} e aparece na posição ', end='')
    for c in range(0, len(posmaior)):
        print(f'{posmaior[c]}... ', end='')

if len(posmenor) > 1:
    print(f'\nO menor valor é {min(l)} e aparece nas posições ', end='')
    for c in range(0, len(posmenor)):
        print(f'{posmenor[c]}... ', end='')

if len(posmenor) == 1:
    print(f'\nO menor valor é {min(l)} e aparece na posição ', end='')
    for c in range(0, len(posmenor)):
        print(f'{posmenor[c]}... ', end='')
