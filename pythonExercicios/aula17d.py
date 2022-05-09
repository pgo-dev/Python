a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')

b[2] = 8

print(f'Nova lista B: {b}')
print(f'Nova lista A: {a}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Nova lista B: {b}')
print(f'Nova lista A: {a}')