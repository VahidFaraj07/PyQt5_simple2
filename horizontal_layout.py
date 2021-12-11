import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Horizontal Box Layout')
        self.UI()
        self.show()

    def UI(self):
        horizontalBox = QHBoxLayout()
        button1=QPushButton("File")
        button2=QPushButton("Edit")
        button3=QPushButton("View")
        

        horizontalBox.addWidget(button1)
        horizontalBox.addWidget(button2)
        horizontalBox.addWidget(button3)
        horizontalBox.addStretch()

        self.setLayout(horizontalBox)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
