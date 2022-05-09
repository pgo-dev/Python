l = list()
v = int(input('Digite um valor: '))
print(f'O valor {v} foi adicionado ao final da lista!')
l.append(v)

for c in range(0, 4):
    v = int(input('Digite um valor: '))

    if v > l[len(l)-1]:
        l.append(v)
        print(f'O valor {v} foi adicionado ao final da lista')
    for d in range(0, len(l)):
        if v <=l[d]:
            l.insert(d, v)
            print(f'O valor {v} foi colocado na posição {d}')
            x = False
            break

print(l)

