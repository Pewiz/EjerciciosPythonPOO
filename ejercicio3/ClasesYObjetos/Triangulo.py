import math

class Triangulo:
    def __init__(self, lado, base):
        self.lado = lado
        self.base = base

    def perimetro(self):
        per = self.base + 2 * self.lado
        return per

    def area(self):
        are = (self.base * math.sqrt((self.lado ** 2) - ((self.base ** 2) / 4))) / 2
        return are