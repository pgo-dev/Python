l = []
d = {}
qp = si = 0
qm = []

while True:

    d['Nome'] = str(input('Nome: '))
    qp = qp + 1

    d['Sexo'] = str(input('Sexo: '))
    if d['Sexo'] == 'f':
        qm.append(d['Nome'])

    d['Idade'] = int(input('Idade: '))
    si = d['Idade'] + si

    l.append(d.copy())

    conf = str(input('Deseja continuar? [s/n] ')).strip().lower()
    if conf == 'n':
        break

print(f'Foram cadastradas {qp} pessoas no grupo, e a média de idade é {si/qp:.2f} anos.')

print('As mulheres são:')
for c in range(0, len(qm)):
    print(f'{qm[c]}')

print('As pessoas com idade maior que a média são: ')
for c in l:
    for k, v in c.items():
        if k == 'Idade':
            if v > si/qp:
                print(f'{c["Nome"]}')
