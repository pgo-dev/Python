from random import randint

num = []

def sorteio():
    for c in range(0, 5):
        num.append(randint(1, 9))
    print(num)

def somapar():
    sum = 0
    for c in num:
        if c%2 == 0:
            sum = sum +c
    print(sum)

sorteio()
somapar()