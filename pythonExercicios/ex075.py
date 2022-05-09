t = (int(input('Digite o primeiro valor:')),
     int(input('Digite o segundo valor:')),
     int(input('Digite o terceiro valor:')),
     int(input('Digite o quarto valor:')))

if t.count(9) == 0:
    print('Não possui 9 na tupla')
elif t.count(9) == 1:
    print(f'O 9 apareceu uma vez')
else:
    print(f'O 9 apareceu {t.count(9)} vezes')

if 3 in t:
    print(f'O 3 apareceu primeiro na {t.index(3)+1}ª posição')
else:
    print('Não foi digitado 3 na tupla')

for c in t:
    if c % 2 == 0:
        x = True
        break
    else:
        x = False

if x:

    print('Os números pares foram: ', end='')
    for c in range(0, len(t)):
        if t[c]%2 == 0:
            print(t[c], end='; ')
else:
    print('Não existem números pares na tupla')