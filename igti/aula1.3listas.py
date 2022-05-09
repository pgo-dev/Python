from random import randint

lista = []
print(f'Lista vazia: {lista}')
print(type(lista))

'''for c in range(0, 9):
    lista.append(randint(0, 10))

print(lista)'''

print('-'*50)

lista = ['IGTI', 'MBA', 'Python']
print(f'Lista com várias string: {lista}')
print(lista[0])
print(lista[2])

print('-'*50)
lista = []
lista.append('Azul')
lista.append('Verde')
lista.append('Vermelho')
lista.append('Amarelo')

print(lista)

lista.insert(2, 'Preto')
lista.insert(0, 'Rosa')
print(lista)

print('-'*50)

lista.extend(['Branco','123','456'])
print(lista)

print('-'*50)

lista = [1,2,3,4,5]
lista.remove(5)
print(lista)
lista.remove(lista[2])
print(lista)
