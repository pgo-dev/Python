from random import randint

t = (randint(0, 10),
     randint(0, 10),
     randint(0, 10),
     randint(0, 10),
     randint(0, 10))

print('Os números da tupla são:')

for c in range(0, len(t)):

    if c < len(t)-2:
        print(f'{t[c]}', end=', ')
    elif c < len(t)-1:
        print(f'{t[c]}', end=' e ')
    else:
        print(f'{t[c]}.')

if max(t) != min(t):
    print(f'O maior é {max(t)} e o menor é {min(t)}')
else:
    print(f'O maior e o menor são iguais e valem {max(t)}')
