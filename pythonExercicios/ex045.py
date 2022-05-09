import random

u = str(input('pedra, papel ou tesoura?')).strip()

u0 = u.lower()

if u0 == 'pedra' or u0 == 'papel' or u0 == 'tesoura':

    print('vc escolheu {}'.format(u))

    lista = ['pedra', 'papel', 'tesoura']
    pc = random.choice(lista)
    print('o pc escolheu {}'.format(pc))

    if u0 == pc:
        print('empate')
    elif u0 == 'pedra' and pc == 'tesoura':
       print('vc ganhou')
    elif u0 == 'papel' and pc == 'pedra':
        print('vc ganhou')
    elif u0 == 'tesoura' and pc == 'papel':
        print('vc ganhou')
    else:
        print('vc perdeu')

else:
    print('escolha pedra, papel ou tesoura!')
