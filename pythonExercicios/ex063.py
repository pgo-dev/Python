n = int(input('Digite um número: '))
cat = cant = 0

print('A sequencia de Fibonacci até {} é:'.format(n))

for c in range(0, n-1):
    if c == 0:
        print('{} '.format(c), end='')
        cp = 1
        cat = 1
        print('{} '.format(cp), end='')
    else:
        cp = cat + cant
        print('{} '.format(cp), end='')
        cant = cat
        cat = cp

if n == 0:
    print(n)