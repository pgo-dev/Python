n = input('Digite algo: ')
print('O tipo primitivo é {} !'.format(type(n)))

if n.isalpha():
    print('É alfabético!')
else:
    print('NÃO é alfabético!')

if n.isalnum():
    print('É alfanumérico!')
else:
    print('NÃO é alfanumérico!')

if n.islower():
    print('Possui somente letras minúsculas!')
else:
    print('NÃO possui somente letras minúsculas!')

if n.isupper():
    print('Possui somente letras maiúsculas!')
else:
    print('NÃO possui somente letras maiúsculas!')

if n.isnumeric():
    print('É somente um número')
else:
    print('NÃO é somente um número')

if n.istitle():
    print('Está capitalizada!')
else:
    print('NÃO está capitalizada!')

if n.isspace():
    print('Possui somente espaço!')
else:
    print('NÃO possui somente espaço!')


