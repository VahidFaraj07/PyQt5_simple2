import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Menu Bar Widget')
        self.UI()
        self.show()

    def UI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        code_menu = menu_bar.addMenu('Code')
        help_menu = menu_bar.addMenu('Help')

        action1_menu = QAction('New Project', self)
        file_menu.addAction(action1_menu)

        action2_menu = QAction('Open Project', self)
        action2_menu.setShortcut('Ctrl+O')
        file_menu.addAction(action2_menu)

        action3_menu = QAction('Exit', self)
        action3_menu.setIcon(QIcon('../logo.jpg'))
        action3_menu.triggered.connect(self.exitFunc)
        
        file_menu.addAction(action3_menu)

    def exitFunc(self):
        mes_box = QMessageBox.question(
            self, "Warning", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.No)
        if mes_box == QMessageBox.Yes:
            sys.exit()



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
