import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 500)
        self.setWindowTitle('Grid Layout')
        self.UI()
        self.show()

    def UI(self):
        self.grid_layout = QGridLayout()
        for i in range(0, 3):
            for j in range(0, 3):
                num_button = QPushButton(str(i*3+j+1))
                self.grid_layout.addWidget(num_button, i, j)
                num_button.clicked.connect(self.clickMe)
        self.setLayout(self.grid_layout)

    def clickMe(self):
        button_id = self.sender().text()
        print(button_id)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
