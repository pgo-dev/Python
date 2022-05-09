nome = str(input('Digite seu nome completo: ')).strip()

nome = nome.split()

print('O primeiro nome é {}. '.format(nome[0]))
a = len(nome)
print('O último nome é {}. '.format(nome[len(nome)-1]))

