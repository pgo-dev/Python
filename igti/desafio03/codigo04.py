def funcao4(lista_num):
    print(f'valorpassado {lista_num}')
    a = lista_num[0]
    b = lista_num[-1]
    print(b)

    if (a==b):
        return True
    else:
        return False

numeros = [10, 20, 30, 22, 66, 88, 40, 10]

print(funcao4(numeros))


