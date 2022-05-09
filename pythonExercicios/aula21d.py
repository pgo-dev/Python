def teste():
    x = 8 #variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2 #variável global
print(f'No programa principal, n vale {n}')
teste()
