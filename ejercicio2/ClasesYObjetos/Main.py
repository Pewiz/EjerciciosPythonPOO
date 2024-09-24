from Auto import Auto

class Main():
    def __init__(self):
        self.ejecutar()

    def ejecutar(self):
        autosIngresar = int(input("Cantidad de autos a ingresar: "))

        autos = []

        for i in range(autosIngresar):
            print(f"--AUTO N° {i+1}")
            marca = str(input("Marca: "))
            modelo = str(input("Modelo: "))
            precio = float(input("Precio: "))

            auto = Auto(marca, modelo, precio)

            autos.append(auto)

        

    def autoMasBarato(self, autos):
        precioMenor = autos[0].getPrecio()
        indice = 0

        for i in range(1, len(autos)):
            if autos[i].getPrecio() < precioMenor:
                precioMenor = autos[i].getPrecio()
                indice = i

        return indice

if __name__ == "__main":
    main = Main()
