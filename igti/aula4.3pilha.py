def invertestring(valorstring):
    resultado = ' '
    for c in valorstring:
        resultado = c + resultado

    return resultado

string = input('Entre com uma string: ')

while string.strip() != '':
    print(f'O inverso de {string} é {invertestring(string)}')
    string = input('Entre com uma string ou aperte ENTER para sair: ')

