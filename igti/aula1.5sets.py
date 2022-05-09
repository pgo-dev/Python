conjunto_a = set()
print(f'Conjunto vazio: {conjunto_a}')
print(type(conjunto_a))

print('_'*50)

conjunto_a = set('python')
print(f'Conjunto com uma string: {conjunto_a}')

print('_'*50)

conjunto_a = set(['igti', 'mba', 'igti'])
print(f'Conjunto via lista: {conjunto_a}')

print('_'*50)

conjunto_a = set([1,2,'igti',4, 'mba', 'igti', 'mba'])
print(f'Conjunto com valores diferentes: {conjunto_a}')

print('_'*50)

conjunto_a = set()
print(f'Conjunto vazio: {conjunto_a}')
conjunto_a.add(8)
conjunto_a.add(9)
conjunto_a.add((6, 7))
print(conjunto_a)

conjunto_a.update([10, 11])
print(conjunto_a)


