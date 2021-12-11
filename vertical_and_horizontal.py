import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QHBoxLayout, QCheckBox, QRadioButton, QComboBox, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Vertital and Horizontal Box Layout')
        self.UI()
        self.show()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()

        chckBX = QCheckBox()
        rdBtn = QRadioButton()
        cmbBx = QComboBox()

        btn1 = QPushButton('Save')
        btn2 = QPushButton('Exit')

        topLayout.addWidget(chckBX)
        topLayout.addWidget(rdBtn)
        topLayout.addWidget(cmbBx)
        topLayout.setContentsMargins(5, 5, 400, 200)

        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)

        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    


if __name__ == '__main__':
    main()
