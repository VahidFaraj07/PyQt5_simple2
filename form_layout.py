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
        formLayout = QFormLayout()

        userName = QLabel('Username:')
        userPass = QLabel('Password:')

        

        inputUserN = QLineEdit()
        inputUserP = QLineEdit()

        formLayout.addRow(userName, inputUserN)
        formLayout.addRow(userPass, inputUserP)
        
        inputUserP.setEchoMode(QLineEdit.Password)

        powerBtnBox = QHBoxLayout()
        powerBtnBox.addStretch()
        powerBtnBox.addWidget(QPushButton('Enter'))
        powerBtnBox.addWidget(QPushButton('Exit'))

        formLayout.addRow(powerBtnBox)

        self.setLayout(formLayout)
        



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
