s = float(input('Digite seu salário: R$'))

if s > 1250:
    print('salario alto')
    s = s*1.1
    print('Seu novo salário é de: {} reais.'.format(s))
else:
    print('salario baixo')
    s = s * 1.15
    print('Seu novo salário é de: {} reais.'.format(s))
