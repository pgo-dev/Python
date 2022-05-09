total = qmil = pmb = 0
mb = ''

while True:
    n = str(input('Produto: '))
    p = float(input('Preço: R$'))

    total = total + p

    if p > 1000:
        qmil = qmil + 1

    if total == p or p < pmb:
        pmb = p
        mb = n

    while True:
        cont = str(input('Deseja continuar?: [s/n] ')).strip().lower()
        if cont[0] not in 'sn':
            print('Opção inválida.')
        else:
            break

    if cont[0] == 'n':
        break

print(f'O total gasto foi de: R${total:.2f}', end=', ')

if qmil == 0:
    print('')
elif qmil == 1:
    print(f'{qmil} produto custou mais de mil reais e ', end='')
else:
    print(f'{qmil} produtos custaram mais de mil reais e ', end='')

print(f'o produto mais barato foi {mb}')

