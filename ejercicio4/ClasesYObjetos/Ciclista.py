class Ciclista:
    def __init__(self, numeroCiclista, nombre, tiempoCarrera):
        self.numeroCiclista = numeroCiclista
        self.nombre = nombre
        self.tiempoCarrera = tiempoCarrera
    
    def getTiempoCarrera(self):
        return self.tiempoCarrera

    def datos_ciclista(self):
        return f"\nN°{self.numeroCiclista}\nNombre: {self.nombre}\nTiempo: {self.tiempoCarrera}"

