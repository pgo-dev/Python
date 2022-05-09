import datetime

an = int(input('Ano de nascimento:'))

#aa = datetime.date.today().year
aa = 2017

d = aa - an

if d > 18:
    print('Passou do alistamento {} anos'.format(d-18))
elif d < 18:
    print('Se alistará em {} anos'.format(18-d))
else:
    print('Ano de alistamento, vc tem {} anos'.format(d))

