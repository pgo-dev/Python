t = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo',
     'Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos',
     'Bahia','Fluminense','Corinthians','Chapecoense','Ceará',
     'Vasco','Sport','América-MG','Vitória','Paraná')

print('\nLISTA COMPLETA:\n')
for c in t:
    print(c)

print('\nOS CINCO PRIMEIROS DA TABELA SÃO:\n')
for c in range(0, 5):
    print(f'{c+1}º:{t[c]}')

print('\nOS ÚLTIMOS QUATRO DA TABELA SÃO:\n')
for c in range(len(t)-1, len(t)-5, -1):
    print(f'{c+1}º:{t[c]}')

to = sorted(t)

print('\nOS TIMES EM ORDEM ALFABÉTICA SÃO:\n')
for c in sorted(t):
    print(c)

print('\nEM QUAL POSIÇÃO ESTÁ O CHAPECOENSE:\n')
for c in range(0, len(t)):
    if t[c] == 'Chapecoense':
        print(f'O Chapecoense está na {c+1}ª posição')

