nome = str(input('Digite o seu nome: ')).strip()

nome = nome.lower().find('silva')

if nome >= 0:
   print('Possui Silva')
else:
    print('Não possui Silva')
