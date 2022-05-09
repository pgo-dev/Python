l = list()
lp = list()
li = list()
cont = 0

while True:

    l.append(int(input(f'Digite o {cont + 1}º valor da lista: ')))

    while True:
        confirm = str(input('Deseja continuar: [S/N]: ')).lower().strip()
        if confirm not in 'sn':
            print('Digite uma opção válida!')
        else:
            break

    if l[cont] % 2 == 0:
        lp.append(l[cont])
    else:
        li.append(l[cont])

    cont = cont + 1

    if confirm == 'n':
        break
    elif confirm == 's':
        print('', end='')

print(f'A lista completa é {l}')
print(f'A lista dos pares é {lp}')
print(f'A lista dos impares é {li}')
