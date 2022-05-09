def leiaint(n):
    while True:
        if n.isnumeric():
            return f'Número {n} digitado'
        else:
            print('ERRO!')
            n = str(input('Digite um número inteiro: '))

n = str(input('Digite um número inteiro: '))
print(leiaint(n))
