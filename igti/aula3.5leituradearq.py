nome = input(str('Insira o nome do arquivo a ser lido: '))

arquivo = open(nome+'.txt', 'r')

for linhas in arquivo:
    print(linhas)
arquivo.close()

print('-'*50)
linhas = 0
arquivo = open(nome+'.txt', 'r')

for linhas in arquivo:
    print(linhas.rstrip())

arquivo.close()

