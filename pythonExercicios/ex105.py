def notas(l, sit=False):
    sum = 0
    maior = menor = l[0]

    for c in range(0, len(l)):

        sum = sum + l[c]
        if l[c] > maior:
            maior = l[c]
        if l[c] < menor:
            menor = l[c]

    dic = {}
    dic['Quantidade de Notas'] = c +1
    dic['Maior nota'] = maior
    dic['Menor nota'] = menor
    dic['Média'] = sum/(c + 1)

    if sit == True:
        if dic['Média'] >= 6:
            dic['Situação'] = 'Boa'
        else:
            dic['Situação'] = 'Ruim'

    return dic

lista = []
cont = 0

while True:
    n = float(input(f'Digite a {cont + 1}º nota: (999 para sair) '))
    if n == 999:
        break
    lista.append(n)
    cont = cont + 1

print(notas(lista))
print(notas(lista, True))