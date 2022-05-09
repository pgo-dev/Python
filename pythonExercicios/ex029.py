from math import floor

v = float(input('Qual velocidade do carro em km/h? '))

if v > 80:

    v = floor(v)
    print(v)
    m = (v - 80)*7

    print('Seu carro foi multado e a multa é de {:.2f} reais'.format(m))
else:
    print('Você está dentro do limite de velocidade!')
