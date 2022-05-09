frase = str(input('Digite uma frase qualquer:')).strip().lower()

print('A letra "a" aparece {} vezes.'.format(frase.count('a')))

print('A letra "a" aparece primeiro na {}ª posição'.format(frase.find('a')+1))

print('A letra "a" aparece pela última vez na {}ª posição'.format(frase.rfind('a')))
