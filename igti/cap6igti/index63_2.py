from aula6_3 import Formas

class Quadrado(Formas):
    def __init__(self, x):
        super().__init__(x, x)

class Cubo(Quadrado):
    def area_da_superficie(self):
        area_da_face = super().area()
        return area_da_face*6

    def volume(self):
        area_da_face = super().area()
        return area_da_face*self.x

quadrado = Quadrado(6)

print(quadrado.get_perimetro())
print(quadrado.area())

cubo = Cubo(3)
print(cubo.volume())
print(cubo.area_da_superficie())

print(issubclass(Cubo, Quadrado))
print(issubclass(Cubo, Formas))


