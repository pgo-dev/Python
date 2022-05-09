def leiaint(msg=''):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Opção inválida! ')
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = str(input(msg))
            n = n.replace(',', '.')
            n = float(n)
        except:
            print('Opção inválida! Digite um número real: ')
        else:
            return n

def leiastr(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            if n.isnumeric() or n == '':
                print('Opção inválida!')
            else:
                return n
        except:
            print('Opção inválida!')



'''m = 'Digite um número inteiro: '
n = leiaint(m)

print(f'Você digitou o número inteiro {n}')

m = 'Digite um número real: '
n = leiafloat(m)

print(f'Você digitou o número real {n:.2f}')'''
