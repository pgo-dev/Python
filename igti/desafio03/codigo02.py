def funcao2(num):
    num_anterior = 0
    for i in range(num):
        resultado= num_anterior + 1
        print(f'Numero A {i}. Numero B {num_anterior}. Resultado {resultado}')
        num_anterior = i

funcao2(10)

