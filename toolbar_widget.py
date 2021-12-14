import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Menu Bar Widget')
        self.UI()
        self.show()

    def UI(self):
        main_tBar = self.addToolBar("myToolBar")

        main_tBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        subBar_new = QAction(QIcon('logo/folder.png'), 'New', self)
        main_tBar.addAction(subBar_new)
        


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
