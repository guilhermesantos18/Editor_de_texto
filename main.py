import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QListWidgetItem, QMainWindow


def say_hello():
    print("Button clicked, Hello!")


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Arquivo de Texto')
        # Classes para ajudar na criação do aplicativo
        self.layout = QVBoxLayout(self)
        # Criar um botao e conectá-lo a uma função para fazer algo
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.say_hello)
        self.layout.addWidget(self.button)
        # Lista de opções

    def say_hello(self):
        print("Button clicked, Hello!")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # Run the main Qt loop
    sys.exit(app.exec())
