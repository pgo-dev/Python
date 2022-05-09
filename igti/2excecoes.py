idades = {'Túlio': 30, 'Maria': 28, 'Antônio': 33}
pessoa = input('Quero saber a idade de: ')

idade = idades.get(pessoa)
print(type(idade))

if idade:
    print(f'{pessoa} tem idade {idade} anos de idade.')
else:
    print(f'{pessoa} com idade desconhecida')