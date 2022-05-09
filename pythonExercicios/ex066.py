s = n = cont = 0

while True:
    n = int(input('Digite um número: (999 para sair)'))
    if n == 999:
        break
    s = s + n
    cont = cont + 1

print(f'Foram digitados {cont} números e a soma entre eles vale: {s}')
