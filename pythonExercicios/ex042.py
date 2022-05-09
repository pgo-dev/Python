l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

maior = l1
l11 = l2
l12 = l3

if l2 > maior and l2 > l3:
    maior = l2
    l11 = l1
    l12 = l3
if l3 > maior and l3 > l2:
    maior = l3
    l11 = l2
    l12 = l1

print(maior)
print(l11)
print(l12)

if l11 + l12 <= maior:
    print('Essas medidas não formam um triângulo')

elif l11 == l12 and l11 == maior and l12 == maior:
    print('triângulo equilátero')

elif l11 != l12 and l12 != maior and l11 != maior:
    print('triângulo escaleno')

else:
    print('triângulo isóceles')
