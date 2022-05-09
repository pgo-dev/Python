for c in range(0, 5):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))

    if c == 0:
        maior = p
        menor = p

    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

if maior == menor:
    print('Todos pesam a mesma coisa')
else:
    print('mais pesado: {}; menos pesado: {}'.format(maior, menor))
