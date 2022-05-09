f = str(input('digite uma frase: ')).strip().lower()
f = f.replace(' ', '')

for c in range(0, len(f)):
    if f[c] == f[len(f)-(c+1)]:
        print('', end='')
    else:
        print('Não é palíndromo')
        break

if c == len(f)-1:
    print('É palíndromo')
