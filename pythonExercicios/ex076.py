l = ('Pão', 1,
     'Manteira', 2.5,
     'Queijo',5,
     'Suco', 4)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS:":^40}')
print('-'*40)

for c in range(0, len(l), 2):
    print(f'{l[c]:.<33}', f'R${l[c + 1]:.2f}')

print('-'*40)
