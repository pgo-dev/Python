sum = 0
qm = 0
hm = ''

for c in range(0, 4):
    n = str(input('Digite o nome da {}ª pessoa: '.format(c+1))).strip()
    i = float(input('Digite a idade da pessoa: '))
    s = str(input('Digite o "m" para sexo masculino e "f" para sexo feminino: ')).strip()

    sum = sum + i

    if c == 0 and 'm':
        v = i
        hm = n
    else:
        if s.lower() == 'f' and i <= 20:
            qm = qm + 1
        if s.lower() == 'm' and i > v:
            hm = n
            v = i

m = sum/(c+1)
print('A média de idade do grupo é: {:.1f}'.format(m))

if hm == '':
    print('Não existem homens no grupo')
else:
    print('O homem mais velho é {}'.format(hm))

if qm > 0:
    print('Tem {} mulher(es) menores de 20 anos.'.format(qm))
else:
    print('Não existem mulheres com menos de 20 anos no grupo')
