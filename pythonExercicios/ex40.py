n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2)/2
print('sua média é {:.1f}'.format(m))
if 5 <= m <= 6.9:
    print('recuperação'.format(m))
elif m > 6.9:
    print('aprovado'.format(m))
else:
    print('reprovado'.format(m))
