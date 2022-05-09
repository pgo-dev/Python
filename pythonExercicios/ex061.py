p = int(input('primeiro termo da PA: '))
r = int(input('razão da PA: '))
c = 0

while c < 10:
    print('{} '.format(p+r*c), end=' ')
    c = c + 1
