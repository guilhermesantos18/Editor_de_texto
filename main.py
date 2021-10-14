import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog
from PySide6.QtGui import QIcon


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
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        menu_bar = self.menuBar()
        filemenu = QMenu('File', self)
        menu_bar.addMenu(filemenu)
        botao_new = filemenu.addAction(QIcon('novodocumento.ico'), 'New')
        botao_new.triggered.connect(lambda: self.new_file())
        botao_open = filemenu.addAction(QIcon('abrirdocumento.ico'), 'Open')
        botao_open.triggered.connect(lambda: self.open_file())
        botao_save = filemenu.addAction(QIcon('salvar.ico'), 'Save')
        botao_save.triggered.connect(lambda: self.save_file())

    def save_file(self):
        # save_file = QFileDialog.saveFileContent()
        pass

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open text", "", "Text files (*.txt)")

    def new_file(self):
        pass


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # Run the main Qt loop
    sys.exit(app.exec())
