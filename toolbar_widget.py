import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Toolbar Widget')
        self.UI()
        self.show()

    def UI(self):
        main_tBar = self.addToolBar("myToolBar")

        main_tBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        subBar_new = QAction(QIcon('logo/empty.png'), 'New', self)
        main_tBar.addAction(subBar_new)
        
        subBar_open = QAction(QIcon('logo/folder.png'), 'Open', self)
        main_tBar.addAction(subBar_open)

        subBar_save = QAction(QIcon('logo/save.png'), 'Save', self)
        main_tBar.addAction(subBar_save)

        subBar_exit = QAction(QIcon('logo/exit.png'), 'Exit', self)
        main_tBar.addAction(subBar_exit)
        subBar_exit.triggered.connect(self.exitFunc)

        # all action in one func
        main_tBar.actionTriggered.connect(self.allActionInOne)



    def exitFunc(self):
        mes_box = QMessageBox.question(
            self, "Warning", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.No)
        if mes_box == QMessageBox.Yes:
            sys.exit()

    def allActionInOne(self, action_type):
        if action_type.text() == 'New':
            print('New')

        elif action_type.text() == 'Open':
            print('Open')

        elif action_type.text() == 'Save':
            print('Save')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
