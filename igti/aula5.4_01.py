class Carro:
    def __init__(self, numero_portas, preco):
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instaciado com sucesso')

    def get_numero_portas(self):
        return self.numero_portas

carro_1 = Carro(4, 50000)

portas_carro_1 = carro_1.get_numero_portas()
print(f'Meu carro possui {portas_carro_1} portas')

carro_2 = Carro(2, 80000)
portas_carro_2 = carro_2.get_numero_portas()
print(f'Meu carro possui {portas_carro_2} portas')

print(f'Endereço memória carro_1: {hex(id(carro_1))}')
print(f'Endereço memória carro_2: {hex(id(carro_2))}')
