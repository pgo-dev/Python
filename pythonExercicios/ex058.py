from random import randint

n = 11
npc = randint(0, 10)

while n != npc:
    n = int(input('Digite um número de 0 a 10: '))
    if n != npc:
        print('Tente novamente!')
print('Acertou!')
print(npc)