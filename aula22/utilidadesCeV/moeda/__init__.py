def aumentar(m, p=0, par=False):
    if par:
        return f'R${m*((p/100)+1):.2f}'
    else:
        return m*((p/100)+1)

def diminuir(m, p=0, par=False):
    if par:
        return f'R${m * (1-(p / 100)):.2f}'
    else:
        return m * (1-(p / 100))

def dobro(m, par=False):
    if par:
        return f'R${2*m:.2f}'
    else:
        return 2*m

def metade(m, par=False):
    if par:
        return f'R${m/2:.2f}'
    else:
        return m/2

def moeda(m, par=False):
    if par:
        return f'R${m:.2f}'
    else:
        return m

def resumo(m, a, d):
   print(f'Preço analizado: {moeda(m, par=True)}')
   print(f'Dorbro do preço: {dobro(m, par=True)}')
   print(f'Metade do preço: {metade(m, par=True)}')
   print(f'80% de aumento: {aumentar(m, a, par=True)}')
   print(f'35% de redução: {diminuir(m, d, par=True)}')

