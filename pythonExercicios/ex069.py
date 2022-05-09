qi = qh = qm20 = 0

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Sexo: [m/f] ')).strip().lower()

    if idade > 18:
        qi = qi + 1
    if 'm' in sexo[0]:
        qh = qh + 1
    if 'f' in sexo[0] and idade < 20:
        qm20 = qm20 +1

    while True:
        cont = str(input('Deseja continuar?: [s/n] ')).strip().lower()
        if cont[0] not in 'sn':
            print('Opção inválida.')
        else:
            break

    if 'n' in cont[0]:
        break

if qi == 1:
    print(f'{qi} pessoa tem mais de 18 anos', end=', ')
else:
    print(f'{qi} pessoas tem mais de 18 anos', end=', ')

if qh == 0:
    print('não existem homens no grupo', end=' e ')
elif qh == 1:
    print(f'existe {qh} homem no grupo', end=' e ')
else:
    print(f'existem {qh} homens no grupo', end=' e ')

if qm20 == 0:
    print('não existem mulheres no grupo com menos de 20 anos.')
elif qm20 == 1:
    print(f'existe {qm20} mulher no grupo com menos de 20 anos.')
else:
    print(f'existem {qm20} mulheres no grupo com menos de 20 anos.')
