filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} do filme é {v}')
