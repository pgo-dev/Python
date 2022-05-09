l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

s = l * a
q = s/2

print('A área da parede é {:.2f} m² e a será necessário {:.2} litros de tinta para pintá-la'.format(s, q))
