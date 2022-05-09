n = cont = sum = 0

while n != 999:
    sum = sum + n
    cont = cont + 1
    n = int(input('Digite um número inteiro: '))

print('Vc digitou {} números e a soma entre ele é {}.'.format(cont - 1, sum))
