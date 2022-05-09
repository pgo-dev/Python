from random import randint
from time import sleep

l = list()
t = list()
q = int(input('Quantos jogos você quer? '))

for c in range(0, q):
    for d in range(0, 6):
        n = randint(1, 60)

        if d == 0:
            t.append(n)
        else:
            t.append(n)
            for e in range(1, len(t)):
                if n == t[e-1]:
                    t.remove(n)
                    print('removeu')
                    t.append(randint(1, 60))
                    break

    t.sort()
    l.append(t[:])
    t.clear()

for c in l:
    print(c)
    sleep(1)
