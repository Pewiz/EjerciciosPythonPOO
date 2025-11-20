import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt


class VentanaInteractiva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0  
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setWindowTitle("Boton Interactivo")
        self.setGeometry(100, 100, 400, 300)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout = QVBoxLayout()

        self.etiqueta = QLabel("Haz click en el botón")
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.etiqueta)

        self.boton = QPushButton("Haz Click Aquí")

        self.boton.clicked.connect(self.cuando_click)
        
        layout.addWidget(self.boton)

        self.boton_reiniciar = QPushButton("Reiniciar Contador")
        self.boton_reiniciar.clicked.connect(self.reiniciar_contador)
        layout.addWidget(self.boton_reiniciar)

        widget_central.setLayout(layout)
    
    def cuando_click(self):

        self.contador += 1
        self.etiqueta.setText(f"Has hecho click {self.contador} veces")

        if self.contador == 1:
            self.boton.setText("Haz click otra vez")
        elif self.contador >= 5:
            self.boton.setText(f"Ya llevas {self.contador} clicks")
        else:
            self.boton.setText(f"Click {self.contador + 1}")
    
    def reiniciar_contador(self):
        self.contador = 0
        self.etiqueta.setText("Contador reiniciado. Haz click en el botón!")
        self.boton.setText("Haz Click Aquí")


def main():
    app = QApplication(sys.argv)
    ventana = VentanaInteractiva()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
