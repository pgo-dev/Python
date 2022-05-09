vc = float(input('Valor do imóvel: '))
s = float(input('Salário: '))
t = float(input('Tempo de financimento em anos: '))

p = vc/(t*12)
print('Valor da prestação mensal: {:.2f} reais'.format(p))

if p > s*0.3:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
