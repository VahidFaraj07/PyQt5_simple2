import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('TAB Widget')
        self.UI()
        self.show()

    def UI(self):
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, 'File')
        self.tabs.addTab(self.tab2, 'View')
        self.tabs.addTab(self.tab3, 'Exit')
        main_layout.addWidget(self.tabs)
################################################

        ver_box1 = QVBoxLayout()
        ver_box1.addWidget(QLabel('This is File TAB'))
        self.tab1.setLayout(ver_box1)

        ver_box2 = QVBoxLayout()
        ver_box2.addWidget(QLabel('This is View TAB'))
        self.tab2.setLayout(ver_box2)

        ver_box3 = QVBoxLayout()
        ver_box3.addWidget(QLabel('This is Exit TAB'))
        self.tab3.setLayout(ver_box3)


        self.setLayout(main_layout)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
