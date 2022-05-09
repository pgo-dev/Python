pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade': 22}

print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('\n', end='')

for k in pessoas.keys():
    print(k)
print('\n', end='')

for k in pessoas.values():
    print(k)
print('\n', end='')

for k in pessoas.items():
    print(k)
print('\n', end='')

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n', end='')
