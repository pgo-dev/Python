#exemplo de desempacotamento

def contador(*num):
    soma = 0
    for c in num:
        soma = soma + c
    print(f'A soma é: {soma}')

contador(2, 1, 7)
contador(8, 9)
contador(4, 4, 7, 6, 2)