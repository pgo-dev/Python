try:
    num = int(input('Numerador: '))
    den = int(input('Denominador: '))
except Exception as e:
    print(f'O erro 01 foi {e}')

try:
    if num % den == 0:
        print('O numerador é divisível pelo denominador')
    else:
        print('A divisão não é inteira')

except Exception as er:
    print(f'O erro 02 foi {er}')