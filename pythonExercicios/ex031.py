d = float(input('Digite a distância da viagem em km: '))

if d <= 200:
    p = 0.5 * d
    print('A passagem custará {:.2f} reais.'.format(p))
else:
    p = 0.45 * d
    print('A passagem custará {:.2f} reais.'.format(p))
