import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt


class VentanaBasica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setWindowTitle("Holaaaa c:")
        
        # Establecer tamaño de la ventana (ancho, alto)
        # Nota: setGeometry(x, y, ancho, alto)
        # x, y: posición en pantalla
        # ancho, alto: dimensiones de la ventana
        self.setGeometry(100, 100, 400, 300)

def main():
    app = QApplication(sys.argv)

    ventana = VentanaBasica()
 
    ventana.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

