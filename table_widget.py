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
        ver_box = QVBoxLayout()
        self.main_table = QTableWidget()
        btn_get = QPushButton('Get')

        btn_get.clicked.connect(self.get_value)

        self.main_table.setRowCount(3)
        self.main_table.setColumnCount(4)

        self.main_table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.main_table.setHorizontalHeaderItem(1, QTableWidgetItem('Surname'))
        self.main_table.setHorizontalHeaderItem(2, QTableWidgetItem('Age'))
        self.main_table.setHorizontalHeaderItem(3, QTableWidgetItem('Address'))

        # for hiding row number
        self.main_table.verticalHeader().hide()

        self.main_table.setItem(0, 0, QTableWidgetItem('Alex'))
        self.main_table.setItem(1, 0, QTableWidgetItem('Jason'))
        self.main_table.setItem(2, 0, QTableWidgetItem('Sirius'))

        # for unedited cells
        self.main_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        ver_box.addWidget(self.main_table)
        ver_box.addWidget(btn_get)

        self.setLayout(ver_box)

    def get_value(self):
        for item in self.main_table.selectedItems():
            print(item.text(), item.row(), item.column())


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
