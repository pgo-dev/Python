def comand(a):

    help(a)


while True:

    comando = str(input('Digite um comando para analizar: (digite FIM para sair) ')).strip().lower()

    if comando == 'fim':
        break

    comand(comando)