import math

n = float(input('Digite um número: '))

m = math.floor(n)
m2 = math.ceil(n)

print('O número {} tem a parte intera {}'.format(n, m))
print(m2)

n = float(input('Digite um valor: '))
print('O valor {} tem a parte interia {}'.format(n, int(n)))
