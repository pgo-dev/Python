pares = impares = 0
n = 1

while n != 0:
    n = int(input('digite um valor: '))

    if n != 0:
        if n % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

print('{} pares e {} ímpares'.format(pares, impares))
print('\nFIM')