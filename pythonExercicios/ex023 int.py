num2 = int(input('Digite outro número de 0 a 9999: '))

m = (num2 / 1000)
m = m - m % 1
m = m % 10
print('O milhar é {:.0f}'.format(m))

c = num2 / 100
c = c - c % 1
c = c % 10
print('A centena é {:.0f}'.format(c))

d = num2 / 10
d = d - d % 1
d = d % 10
print('A dezena é {:.0f}'.format(d))

u = num2 / 1
u = u - u % 1
u = u % 10
print('A unidade é {:.0f}'.format(u))
