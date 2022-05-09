nome = str(input('Digite seu nome completo: ')).strip()

print('O nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('O objeto string possui {} blocos.'.format(len(nome)))
print('O nome tem {} espaços'.format(nome.count(' ')))

nomes = len(nome) - nome.count(' ')

print('\nO nome possui {} letras.'.format(nomes))

pnome = nome.split()

print('O primeiro nome tem {} letras.'.format(len(pnome[0])))

#nomed = nome.split()
#print(count.len(nomed[0]))
