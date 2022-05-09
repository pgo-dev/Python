from datetime import date
pessoa = dict()

tap = 35
aa = date.today().year

pessoa['Nome'] = str(input('Nome: '))
an = int(input('Ano de nascimento: '))
idade = aa - an
pessoa['Idade'] = idade
pessoa['Carteira de Trabalho'] = int(input('Nº da CTPS: '))


if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Idade de aposentadoria'] = pessoa['Ano de contratação'] + tap - an
    print()
    for k, v in pessoa.items():
        print(f'{k} = {v}')
else:
    pessoa['Carteira de Trabalho'] = 'não possui carteira de tabalho'
    print()
    for k, v in pessoa.items():
        print(f'{k} = {v}')

