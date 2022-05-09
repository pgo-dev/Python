p = float(input('Digite seu peso em kg: '))
a = float(input('Digite sua altura em m: '))

imc = p/(a**2)
print('{:.2f}'.format(imc))

if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')