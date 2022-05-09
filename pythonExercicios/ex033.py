n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:

    print('{} é o maior!'.format(n1))

    if n2 > n3:
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n2))
else:
    if n2 > n3:
        print('{} é o maior!'.format(n2))
        if n1 > n3:
              print('{} é o menor'.format(n3))
        else:
            print('{} é o menor'.format(n1))
    else:
        print('{} é o maior!'.format(n3))
        if n1 > n2:
              print('{} é o menor'.format(n2))
        else:
            print('{} é o menor'.format(n1))
