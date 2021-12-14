import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 380)
        self.setWindowTitle('Open File Dialogs')
        self.UI()
        self.show()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(5, 5)
        self.editor.setAcceptRichText(False)  # disable different text fonts
        self.editor.resize(490, 300)

        browse_button = QPushButton('Browse', self)
        browse_button.move(10, 340)
        browse_button.clicked.connect(self.fileOpener)

    def fileOpener(self):
        temp_loc = QFileDialog.getOpenFileName(
            self, 'Open a file', '', 'All Files(*);;*txt')
        file_loc = temp_loc[0]
        my_file = open(file_loc, 'r')
        content_file = my_file.read()
        self.editor.setText(content_file)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
