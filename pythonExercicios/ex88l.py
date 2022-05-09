from random import randint
from time import sleep

t = list()

while True:
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
    print(t)
    t.clear()
    sleep(1)



