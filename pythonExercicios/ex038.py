n1 = int(input('n1: '))
n2 = int(input('n2: '))

if n1 > n2:
    print('n1, {}, é maior'.format(n1))
elif n2 > n1:
    print('n2, {}, é maior'.format(n2))
else:
    print('Os dois são iguais, {}, {}'.format(n1, n2))
