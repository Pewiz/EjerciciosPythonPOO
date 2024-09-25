from Ciclista import Ciclista

def ganador(ciclistas):
    tiempo_ganador = ciclistas[0].getTiempoCarrera()
    indice = 0

    for i, ciclista in enumerate(ciclistas):
        if ciclista.getTiempoCarrera() < tiempo_ganador:
            tiempo_ganador = ciclista.getTiempoCarrera()
            indice = i

    print(ciclistas[indice].datos_ciclista())

def main():
    n_ciclistas = int(input("Ingrese la cantidad de ciclistas: "))
    ciclistas = []

    for i in range(n_ciclistas):
        print(f"-- DATOS CICLISTA N°{i + 1} --")
        numero_ciclista = int(input("Número Ciclista: "))
        nombre = input("Nombre: ")
        tiempo_carrera = float(input("Tiempo: "))

        ciclista = Ciclista(numero_ciclista, nombre, tiempo_carrera)
        ciclistas.append(ciclista)

    print("\n--El ganador es: --")
    ganador(ciclistas)

if __name__ == "__main__":
    main()