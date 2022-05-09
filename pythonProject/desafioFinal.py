def cadastraFunc(q):
    nome = input(f'Digite o nome do {q}º funcionário: ')
    sal = float(input(f'Digite o salário bruto do {q}º funcionário: '))
    func.append(f'{q};{nome};{sal:.2f}')
    print('Lista de funcionários cadastrados: ')
    for i in func:
        print(i.split(';')[0], i.split(';')[1], i.split(';')[2])


def calcCheq(i):
    nome = func[i - 1].split(';')[1]
    salario = float(func[i - 1].split(';')[2])
    print(f'{nome} tem salário bruto de R${salario:.2f} por mês')
    print(f'O desconto no INSS é de R${descInss(salario):.2f}. ')
    print(f'O desconto no IRRF é de R${descIrrf(salario):.2f}. ')
    print(f'Seu salário liquido é de R${salario - descInss(salario) - descIrrf(salario):.2f}')


def descIrrf(sal):
    if (sal - descInss(sal)) <= 1903.98:
        return 0
    elif (sal - descInss(sal)) <= 2826.65:
        return (sal - descInss(sal)) * 0.075 - 142.8
    elif (sal - descInss(sal)) <= 3751.05:
        return (sal - descInss(sal)) * 0.15 - 354.8
    elif (sal - descInss(sal)) <= 4664.68:
        return (sal - descInss(sal)) * 0.225 - 636.13
    else:
        return (sal - descInss(sal)) * 0.275 - 869.36


def descInss(sal):
    a1 = 82.5
    a2 = 99.31
    a3 = 132.21
    a4 = 437.97

    if sal <= 1100:
        return sal * 0.075
    elif sal <= 2203.48:
        return a1 + (sal - 1100.01) * 0.09
    elif sal <= 3305.22:
        return a1 + a2 + (sal - 2203.49) * 0.12
    elif sal <= 6433.57:
        return a1 + a2 + a3 + (sal - 3305.23) * 0.14
    else:
        return a1 + a2 + a3 + a4


func = list()
q = 1

cadastraFunc(q)
q = q + 1

while True:
    ctrl = input(
        'Digite "C" para cadastrar novo funcioário ou o índice para imprimir o contracheque dele: (0 para sair) ').lower().strip()
    if ctrl == '0':
        break
    elif ctrl == 'c':
        cadastraFunc(q)
        q = q + 1
    elif ctrl.isnumeric() and int(ctrl) <= len(func):
        calcCheq(int(ctrl))
    else:
        print('Digite uma opção válida!')
