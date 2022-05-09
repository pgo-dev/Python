def fatorial(n):
    if n == 0:
        return 1
    return n*fatorial(n-1)

while True:
    try:
        num = int(input('Digite um número: '))
        print(fatorial(num))
    except:
        break

print('fim')