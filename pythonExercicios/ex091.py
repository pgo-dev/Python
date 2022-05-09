from random import randint
from time import sleep

jogo = dict()
list = list()
listjogo = []

for c in range(0, 4):
    jogo[f'jogador {c+1}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(.5)
    list.append(v)
    list.append(k)

    listjogo.append(list[:])
    list.clear()

listjogo.sort(reverse=True)

for c in range(0, 4):
    print(f'Em {c+1}º lugar o {listjogo[c][1]} com {listjogo[c][0]}')
    sleep(.5)




