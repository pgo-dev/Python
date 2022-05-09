n1 = int(input('Digite um número: '))
n = n1
f = 1

if n1 > 0:
    while n != 1:
        f = f * n
        n = n - 1
    print('{}! é {}'.format(n1, f))
else:
    print('0! é 0')
