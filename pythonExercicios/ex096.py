def area(l, c):
    area = l*c
    print(f'A área do terreno mede: {area:.2f} m²')

larg = float(input('Digite a largura do terreno em m: '))
comp = float(input('Digite o comprimento do terreno em m: '))

area(larg, comp)
