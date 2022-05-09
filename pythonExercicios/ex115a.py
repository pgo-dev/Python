from ex113 import leiaint, leiastr

try:
    f = open('lp.txt', 'x')
except:
    print('Falha ao abrir o arquivo', end='')

while True:
    print('-'*40)
    print('             MENU PRINCIPAL')
    print('-'*40)

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')

    print('-' * 40)

    while True:
        i = leiaint()
        if i == 1 or i == 2 or i == 3:
            break
        else:
            print('Opção inválida! Digite 1, 2 ou 3: ')

    if i == 1:
        print('-' * 40)
        print('            CHAIN LIGHTNING')
        print('-' * 40)
        f = open('lp.txt', 'r')
        print(f.read())
        f.close()

    elif i == 2:
        print('-' * 40)
        print('             NOVO CADASTRO')
        print('-' * 40)
        nome = leiastr('Digite seu nome: ')
        idade = leiaint('Digite sua idade: ')

        f = open('lp.txt', 'a')
        f.write(f'{nome:33}{idade} anos\n')
        f.close()

    elif i == 3:
        break