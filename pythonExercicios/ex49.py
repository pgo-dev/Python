n = int(input('digite o número que vc quer a tabuada: '))

for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(n, c, n*c))
