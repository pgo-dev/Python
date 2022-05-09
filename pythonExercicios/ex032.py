import datetime

a = int(input('Digite o ano (coloque 0 para analisar o ano atual): '))

if a == 0:
    a = datetime.date.today().year

a2 = a / 2

if a2 % 1 == 0 and a % 100 != 0:
    a3 = a2 / 2
    print(a3)
    if a3 % 1 == 0:
        print('O ano {:.0f} é bissexto'.format(a))
    else:
        print('O ano {:.0f} não é bissexto'.format(a))
else:
    print('O ano {:.0f} não é bissexto'.format(a))
