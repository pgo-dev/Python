aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 6:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')