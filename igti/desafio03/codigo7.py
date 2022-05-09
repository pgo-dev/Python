class Classe2():
    def __init__(self, l, w):
        self.a = l
        self.b = w

    def metodo1(self):
        return self.a*self.b

objeto1 = Classe2(12, 10)

print(objeto1.metodo1())
