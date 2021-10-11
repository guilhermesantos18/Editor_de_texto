import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow, QMenu, QMenuBar
from PySide6.QtGui import QIcon, QKeySequence


def say_hello():
    print("Button clicked, Hello!")


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Arquivo de Texto')
        self.createMenu()

    def createMenu(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        menuBar = self.menuBar()
        filemenu = QMenu('File', self)
        menuBar.addMenu(filemenu)
        filemenu.addAction(QIcon('novodocumento.ico'), 'New')
        filemenu.addAction(QIcon('abrirdocumento.ico'), 'Open')
        filemenu.addAction(QIcon('salvar.ico'), 'Save')


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # Run the main Qt loop
    sys.exit(app.exec())
