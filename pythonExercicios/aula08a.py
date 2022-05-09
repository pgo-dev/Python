from math import sqrt
from math import ceil
from math import floor

num = int(input('Digite um número: '))

raiz = sqrt(num)

print('A raiz quadrada de {} é {:.2f} !\n'.format(num, raiz))

print('A raiz quadrada de {}, arredondando para cima é {:.2f} !'.format(num, ceil(raiz)))
print('A raiz quadrada de {}, arredondando baixo é {:.2f} !'.format(num, floor(raiz)))
