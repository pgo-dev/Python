valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor da {cont+1}ª posição: ')))

for c in valores:
    print(f'{c}...')

print(valores)

for c, v in enumerate(valores):
    print(f'A {c+1}ª posição tem o valor {v}. ')

print('FIM!')
