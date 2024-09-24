class Auto:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    def mostrarDatos(self):
        return "Marca: "+self.__marca+"\nModelo: "+self.__modelo+"\nPrecio: "+self.__precio
    