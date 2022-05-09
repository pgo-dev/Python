from time import sleep

p = int(input('primeiro termo da PA: '))
r = int(input('razão da PA: '))
q = int(input('quantos termos da PA: '))

for c in range(p, p+q*r, r):
    sleep(0.2)
    print('{}'.format(c), end=' ')
