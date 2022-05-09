d = {} 
l = []

while True:

    d['Nome do Jogador'] = str(input('Nome do jogador: ')).strip()
    d['Número de partidas'] = int(input('Número de partidas: '))
    np = d['Número de partidas']
    ng = 0

    for c in range(0, np):
        d[f'Gols na partida {c+1}'] = int(input(f'Quantos gols {d["Nome do Jogador"]} fez na partida {c+1}: '))
        ng = d[f'Gols na partida {c+1}'] + ng

    d['Total de gols no campeonato'] = ng

    l.append(d.copy())
    d.clear()

    confirm = str(input('Deseja continuar? [s/n]'))
    if confirm == 'n':
        break

while True:
    x = True
    jog = str(input('Qual jogador deseja visualizar?: ')).strip()

    for c in l:
        for k, v in c.items():
            if jog == v:
                print(f'\nO jogador {c["Nome do Jogador"]} participou de {c["Número de partidas"]} jogos.')
                for d in range(0, len(c)-3):
                    print(f'Na {d+1}º partida fez {c[f"Gols na partida {d+1}"]} gols')
                print(f'E fez um total de {c["Total de gols no campeonato"]} gols no campeonato\n')
                x = False
                break
    if x:
        print(f'{jog} Não faz parte da lista, digite uma opção correta!')