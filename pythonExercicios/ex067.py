while True:
    n = int(input('digite o número que vc quer a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print('{:2} x {:2} = {:2}'.format(n, c, n*c))
print('FIM!')
