n = float(input('Digite um número inteiro: '))

n2 = n/2

if n2 % 1 == 0:
    print('O número {:.0f} é par'.format(n))
else:
    print('O numero {:.0f} é ímpar'.format(n))
