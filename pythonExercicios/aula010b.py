n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = ( n1 + n2 ) / 2

print('A sua média foi {:.2f}'.format(m))

print('Parabéns, você foi aprovado!' if m>=6 else 'Você foi reprovado!')