from datetime import date

an = int(input('ano de nascimento'))

aa = date.today().year

i = aa - an
print(i)

if i <= 9:
    print('mirim')
elif i <= 14:
    print('infantil')
elif i <= 19:
    print('junior')
elif i <= 20:
    print('sênior')
else:
    print('master')