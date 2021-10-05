import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget


def say_hello():
    print("Button clicked, Hello!")


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        # Create a button, connect it and show it
        self.button = QPushButton("Click me")
        self.button.clicked.connect(say_hello)
        self.button.show()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    gui = GUI()
    gui.setMaximumSize(400, 400)
    gui.show()
    # Run the main Qt loop
    app.exec()
