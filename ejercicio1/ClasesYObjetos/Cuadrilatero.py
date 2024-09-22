class Cuadrilatero:
    def __init__(self, lado1, lado2=None):
        if lado2==None:
            self.__lado1= self.__lado2 = lado1
        else:
            self.__lado1 = lado1
            self.__lado2 = lado2
    
    def obtenerArea(self):
        area = self.__lado1 * self.__lado2
        return area
    
    def obtenerPerimetro(self):
        perimetro = 2*(self.__lado1+self.__lado2)
        return perimetro
    
