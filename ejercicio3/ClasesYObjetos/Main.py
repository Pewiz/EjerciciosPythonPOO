from Triangulo import Triangulo

def area_mayor(triangulos):
    areaM = triangulos[0].area()
    for triangulo in triangulos[1:]:
        if triangulo.area() > areaM:
            areaM = triangulo.area()
    return areaM

def main():
    n_triangulo = int(input("Cantidad de triángulos: "))

    triangulos = []

    for i in range(n_triangulo):
        print(f"-- DATOS TRIÁNGULO N°{i + 1} --")
        lado = float(input("Lado: "))
        base = float(input("Base: "))

        triangulo = Triangulo(lado, base)
        triangulos.append(triangulo)
        
        print(f"Área: {triangulo.area()}")
        print(f"Perímetro: {triangulo.perimetro()}")
        print("\n")

    print(f"El área del triángulo con mayor superficie es: {area_mayor(triangulos)}")

if __name__ == "__main__":
    main()