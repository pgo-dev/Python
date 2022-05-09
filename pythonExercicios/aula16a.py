lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print(len(lanche))

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print(enumerate(lanche))
