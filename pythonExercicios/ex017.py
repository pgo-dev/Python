#import math
from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h = hypot(ca, co)
h2 = (co**2 + ca**2)**(1/2)

print('A hipotenusa mede {:.2f}.'.format(h))
print('{:.2f}'.format(h2))
