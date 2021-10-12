import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog
from PySide6.QtGui import QIcon, QKeySequence, QAction


def say_hello(*args):
    print("Button clicked, Hello!")
    print(args)


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
        botao_new = filemenu.addAction(QIcon('novodocumento.ico'), 'New')
        # botao_new.triggered.connect(lambda: say_hello(self))
        botao_open = filemenu.addAction(QIcon('abrirdocumento.ico'), 'Open')
        # botao_open.triggered.connect(lambda: ())
        botao_save = filemenu.addAction(QIcon('salvar.ico'), 'Save')
        botao_save.triggered.connect(lambda: self.salvar_arquivo())

    def salvar_arquivo(self):
        salvar = QFileDialog(self)
        salvar.saveFileContent()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # Run the main Qt loop
    sys.exit(app.exec())
