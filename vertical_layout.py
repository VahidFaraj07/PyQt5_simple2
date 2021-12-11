import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Vertital Box Layout')
        self.UI()
        self.show()

    def UI(self):
        verBox = QVBoxLayout()
        button1 = QPushButton("Save")
        button2 = QPushButton("Exit")

        verBox.addWidget(button1)
        verBox.addWidget(button2)
        verBox.addStretch()
        self.setLayout(verBox)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
