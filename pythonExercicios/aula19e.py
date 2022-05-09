pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade': 22}
del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n', end='')

pessoas['nome'] = 'Leandro'

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n', end='')