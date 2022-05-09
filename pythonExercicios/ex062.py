p = int(input('primeiro termo da PA: '))
r = int(input('razão da PA: '))
c = 0
q = 10
a = 0
x = 1

while True:

        while c < (q + a):
                print('{} '.format(p + r * c), end=' ')
                c = c + 1
        a = int(input('\nQuantos termos vc quer a mais: '))
        q = c

        if a == 0:
                break

print('FIM!')
