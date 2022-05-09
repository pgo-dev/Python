turma = list()
dados = list()

while True:

    dados.append(str(input('Nome: ')).strip().lower())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    m = (dados[1]+dados[2])/2
    dados.append(m)

    turma.append(dados[:])
    dados.clear()

    conf = str(input('Deseja continuar: [s/n] '))
    if conf == 'n':
        break

for c in range(0, len(turma)):
    print(f'A média de {turma[c][0]} foi {turma[c][3]:.2f}.')

while True:
    x = True
    indic = str(input('De quem você deseja ver as notas? ').strip().lower())

    if indic == '999':
        break

    for c in range(0, len(turma)):
        if indic == turma[c][0]:
            print(f'As notas de {turma[c][0]} foram {turma[c][1]} e {turma[c][2]}')
            x = False
            break
    if x == True:
        print('Digite o nome de um aluno dessa turma.')