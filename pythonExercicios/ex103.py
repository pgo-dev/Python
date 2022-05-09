#ROUBADO
def ficha(nome='<desconhecido>', ngols=0):
    print(f'O jogador {nome} fez {ngols} gols no campeonato!')

n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n =='':
    ficha(ngols=g)
else:
    ficha(n, ngols = g)
