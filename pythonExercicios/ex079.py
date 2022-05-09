l = list()
l.append(int(input('Digite um valor para a lista: ')))
a = l[0]

while True:

    while True:
        confirm = str(input('Deseja continuar: [S/N]: ')).lower().strip()
        if confirm not in 'sn':
            print('Digite uma opção válida!')
        else:
            break

    if confirm == 'n':
        break
    elif confirm == 's':
        print('', end='')

    l.append(int(input('Digite um valor para a lista: ')))
    a = l[len(l) - 1]

    for cont in range(0, len(l)-1):
        if a == l[cont]:
            l.pop()
            print('Valor repetido! Ele não será computado!')
            break

print(l)
l.sort()
print(l)
