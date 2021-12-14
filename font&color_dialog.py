import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 360)
        self.setWindowTitle('Font and Color Dialogs')
        self.UI()
        self.show()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(5, 5)
        self.editor.setAcceptRichText(False)  # disable different text fonts
        self.editor.resize(490, 300)

        browse_button = QPushButton('Browse', self)
        browse_button.move(10, 320)
        browse_button.clicked.connect(self.fileOpener)

        color_button = QPushButton('Color', self)
        color_button.clicked.connect(self.changeColor)
        color_button.move(260, 320)

        font_button = QPushButton('Font', self)
        font_button.clicked.connect(self.changeFont)
        font_button.move(380, 320)

    def fileOpener(self):
        temp_loc = QFileDialog.getOpenFileName(
            self, 'Open a file', '', 'All Files(*);;*txt')
        file_loc = temp_loc[0]
        my_file = open(file_loc, 'r')
        content_file = my_file.read()
        self.editor.setText(content_file)

    def changeFont(self):
        my_font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(my_font)

    def changeColor(self):
        my_color = QColorDialog.getColor()
        self.editor.setTextColor(my_color)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
