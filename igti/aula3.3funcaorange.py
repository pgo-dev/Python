for i in range(8):
    print(i)

print('-' * 50)

for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    print(i)

print('-' * 50)

print(type(range(8)))

print('-' * 50)

for i in range(9, 0, -1):
    print(i)

print('-' * 50)

'''string = input(str('Entre com alguma string: '))
for i in range(len(string)):
    print(string[i], end='')
print('\n')
print('-' * 50)

string = input(str('Entre com alguma string: '))

print(len(string))

for i in range(len(string)-1, -1, -1):
    print(string[i], end='')'''

print('-' * 50)

string = 'Estou estudando Python no bootcamp do IGTI'

for c in string.split():
    print(c)
