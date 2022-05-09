lista = ('salsicha',
     'torresmo',
     'pe de pano',
     'home office')

for palavra in lista:
     print(f'\nAs vogais de {palavra} são: ', end='')
     for letra in palavra:
          if letra in 'aeiou':
               print(letra, end=' ')

print('\nFIM')