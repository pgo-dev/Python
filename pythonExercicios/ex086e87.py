linhas = list()
m = list()

for l in range(0, 3):
    for c in range(0, 3):
        linhas.append(int(input(f'Digite o valor da posição {l}, {c}: ')))
    m.append(linhas[:])
    linhas.clear()

contpar = somapar = soma3c = 0
ml2 = list()

for l in range(0, 3):
    for c in range(0, 3):
            print(f'[{m[l][c]:2}] ', end='')

            if m[c][l] % 2 == 0:
                contpar = contpar + 1
                somapar = somapar + m[c][l]

    ml2.append(m[1][l])
    soma3c = soma3c + m[l][2]

    print(end='\n')

print(f'Foram digitados {contpar} valores pares e a soma deles vale {somapar}.')
print(f'A soma dos valores da terceira coluna vale {soma3c}.')
print(f'O maior valor da segunda linha é {max(ml2)}')
