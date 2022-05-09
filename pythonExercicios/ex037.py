n = int(input('Digite um número inteiro: '))
c = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))

if c == 1:
    nb = bin(n)
    print('{} binário é: {}'.format(n, nb[2:]))
elif c == 2:
    no = oct(n)
    print ('{} octal é: {}'.format(n, no[2:]))
elif c == 3:
    nh = hex(n)
    print('{} hexadeceimal é: {}'.format(n, nh[2:]))
else:
    print('tente novamente')

