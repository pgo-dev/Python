valores = list()
pares = list()
impares = list()

for c in range(0, 7):

    v = int(input('Digite um valor: '))

    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

pares.sort()
valores.append(pares[:])
impares.sort()
valores.append(impares[:])
print(f'Os valores pares foram: {valores[0]}')
print(f'Os valores impares foram: {valores[1]}')