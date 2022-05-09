nome_do_arquivo = input(str('Escreva o nome do arquivo a ser criado: '))

nomes = input(str('Digite seu nome: '))
idades = input(str('Digite sua idade: '))
cidades = input(str('Digite sua cidade: '))

arquivo = open(nome_do_arquivo+'.txt', 'w')

arquivo.write(f'{nomes} possui {idades} anos e mora em: {cidades}.\n')

arquivo.write('O rato roeu a roupa do rei de roma')
arquivo.close()
