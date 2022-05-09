valores = list()

valores.append(5)
valores.append(9)
valores.append(4)

for c in valores:
    print(f'{c}...')

print(valores)

for c, v in enumerate(valores):
    print(f'A {c+1}ª posição tem o valor {v}. ')

print('FIM!')
