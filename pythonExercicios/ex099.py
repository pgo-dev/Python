def maior(num):
    m = num[0]
    for c in range(0, len(num)):
        if num[c] > m:
            m = num[c]
    print(m)

l = []

while True:
    n = int(input('Digite um núemro para a lista, digite 999 para parar. '))

    if n == 999:
        break

    l.append(n)

maior(l)