sum = cont = 0
x = 'c'

while x == 'c':
    n = int(input('Digite um número: '))

    if cont == 0:
        maior = menor = n

    x = str(input('Digite "s" para sair ou "c" para continuar: '))
    sum = sum + n
    cont = cont + 1

    if n > maior:
        maior = n
    if n < menor:
        menor = n

print('A média foi {:.2f}, o maior é {} e o menor é {}'.format(sum/cont, maior, menor))
