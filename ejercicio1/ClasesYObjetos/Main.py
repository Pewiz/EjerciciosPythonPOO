# Importamos la clase Cuadrilatero desde otro archivo
from Cuadrilatero import Cuadrilatero

class Main:
    def __init__(self):
        self.ejecutar()

    def ejecutar(self):
        n_cuadrilatero = int(input("Cantidad de cuadriláteros a ingresar: "))

        cuadrilateros = []


        for i in range(n_cuadrilatero):
            print(f"\n--CUADRILÁTERO N° {i + 1}")
            lado1 = int(input("Lado 1: "))
            lado2 = int(input("Lado 2: "))

            if lado1 == lado2:
                cuadrilatero = Cuadrilatero(lado1)
            else:
                cuadrilatero = Cuadrilatero(lado1, lado2)
            
            cuadrilateros.append(cuadrilatero)


        print("\n--RESULTADO--")
        self.mostrar_resultado(cuadrilateros)

    def mostrar_resultado(self, cuadrilateros):
        
        for i, cuadrilatero in enumerate(cuadrilateros):
            print(f"\n--CUADRILÁTERO N° {i + 1}")
            print(f"Área: {cuadrilatero.obtenerArea()}")
            print(f"Perímetro: {cuadrilatero.obtenerPerimetro()}")


if __name__ == "__main__":
    main = Main()
