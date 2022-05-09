from random import randint
cont = 0

while True:
    cond = ' '
    while cond not in 'parimpar':
        cond = str(input('PAR OU ÍMPAR: (escreva sem assento) ')).strip().lower()

    if cond == 'par':
        condpc = 'ímpar'
        print(f'O pc é ímpar')
    else:
        condpc = 'par'
        print(f'O pc é par')

    npc = randint(0, 10)
    n = int(input('Jogue seu número de 0 a 10: '))

    if (n+npc) % 2 == 0 and cond == 'par':
        print(f'\nO pc jogou {npc}')
        print(f'\nA soma deu {n+npc} que é par, então', end=' ')
        print(f'VOCÊ GANHOU jogue novamente')
        cont = cont + 1

    elif (n+npc) % 2 != 0 and cond == 'impar':
        print(f'\nO pc jogou {npc}')
        print(f'\nA soma deu {n + npc}, que é ímpar, então', end=' ')
        print(f'VOCÊ GANHOU, joque novamente.')
        cont = cont + 1

    else:
        print(f'\nO pc jogou {npc}, vc jogou {n}, a soma deu {n + npc} que é {condpc}, então', end=' ')
        print(f'VOCÊ PERDEU pq pediu {cond}! Você venceu {cont} vezes!\n')
        break


