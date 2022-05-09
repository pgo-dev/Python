from datetime import date

def voto(a):
    aa = date.today().year
    idade = aa - a
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade <18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGADTÓRIO'

while True:

    ano = int(input('Digite o seu ano de nascimento: '))

    if ano == 999:
        break

    print(voto(ano))