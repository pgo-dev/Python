class Carro:
    def __init__(self, cor='vermelho', n_portas=3):
        self.cor_do_carro = cor
        self.n_portas_do_carro = n_portas

    def get_cor_carro(self):
        return self.cor_do_carro

    def get_numero_de_portas(self):
        return self.n_portas_do_carro

carro1 = Carro(cor='azul')
carro2 = Carro()
carro3 = Carro(cor='prata')

del carro1.cor_do_carro
print(carro1.get_cor_carro())
