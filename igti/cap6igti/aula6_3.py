class Formas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    descricao = 'A forma ainda não foi definida.'
    autor = 'Ainda não foi definido um autor para ela.'

    def area(self):
        return self.x * self.y

    def get_perimetro(self):
        return 2*self.x + 2*self.y

    def set_descricao(self, texto):
        self.descricao = texto

    def set_nome_do_autor(self, texto):
        self.autor = texto

    def set_escala(self, escala):
        self.x = self.x * escala
        self.y = self.y * escala

class Quadrado(Formas):
    def __init__(self, x):
        self.x = x
        self.y = x
    def get_perimetro_quadrado(self):
        return (self.x)*4
