from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if i > f and p > 0:
        p = p * -1
    elif i < f and p < 0:
        p = p * -1
    elif i == f:
        print(i)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.1)
        if c+p == f:
            print(c+p)

contador(1, 10, 1)
contador(10, 0, 2)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)

