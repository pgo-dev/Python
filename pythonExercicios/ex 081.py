l = list()
cont = 0

while True:

    l.append(int(input(f'Digite o {cont+1}º valor da lista: ')))

    while True:
        confirm = str(input('Deseja continuar: [S/N]: ')).lower().strip()
        if confirm not in 'sn':
            print('Digite uma opção válida!')
        else:
            break

    cont = cont + 1

    if confirm == 'n':
        break
    elif confirm == 's':
        print('', end='')

print('A lista em forma decrescente é: ')
l.sort(reverse=True)

for c in l:
    print(f'{c} ', end=' ')

print(f'\nForam digitados {cont} valores')

if 5 in l:
    print('O valor 5 está na lista')
else:
    print('O valor 5 NÃO está na lista')