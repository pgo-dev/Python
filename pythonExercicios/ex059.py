c = 0

while c != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    c = int(input('Digite 1 para somar, 2 para multiplicar, 3 para saber o maior, 4 para pedir novos números e 5 para sair do programa: '))
    if c == 1:
        r = n1 + n2
        print('A soma é {:.0f}'.format(r))
    elif c == 2:
        r = n1*n2
        print('O produto é {:.0f}'.format(r))
    elif c == 3:
        if n1 > n2:
            print('O primero, {:.0f},  é o maior'.format(n1))
        elif n1 < n2:
            print('O segundo ,{:.0f} , é o maior'.format(n2))
        else:
            print('Eles são iguais!')
    elif c == 4:
        print('', end='')
print('Saiu')