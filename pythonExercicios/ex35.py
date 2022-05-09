l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 > l2 and l1 > l3:
    print('{} pode ser a hipotenusa!'.format(l1))
    h = l1
    c1 = l2
    c2 = l3
elif l2 > l3:
    print('{} pode ser a hipotenusa!'.format(l2))
    h = l2
    c1 = l1
    c2 = l3
else:
    print('{} pode ser a hipotenusa!'.format(l3))
    h = l3
    c1 = l1
    c2 = l2

if c1 + c2 > h:
    print('\nEssas medidas formam um triângulo')
else:
    print('\nEssas medidas não formam um triângulo')