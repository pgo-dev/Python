while True:
    n = int(input('digite um número: '))
    if n == 0 or n == 1:
        print(f'O número {n} NÃO é primo')
    elif n == 2:
        print(f'O número {n} é primo')
    else:
        for c in range(2, n):
            if n % c != 0:
                print('', end='')
                if c + 1 == n:
                    print(f'O número {n} é primo')
            else:
                print(f'O número {n} NÃO é primo')
                break

