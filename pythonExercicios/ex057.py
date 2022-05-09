v = 0
s = str(input('Digite o sexo: ')).lower().strip()[0]

while s not in 'mf':
        s = str(input('Tente novamente, digite seu sexo: ')).lower().strip()[0]

print('Sexo {} registrado.'.format(s))
