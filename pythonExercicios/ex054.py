from datetime import date

maior = 0
menor = 0

for c in range(0, 7):

    a = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c+1)))
    aa = date.today().year
    if aa - a >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} são de maior e {} são de menor'.format(maior, menor))
