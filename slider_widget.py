import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Slider Widget')
        self.UI()
        self.show()

    def UI(self):
        vertBox = QVBoxLayout()

        self.my_slider = QSlider(Qt.Horizontal)
        self.my_text = QLabel("i am a python lover")
        self.temp_text = QLabel(str(self.my_slider.value()))
        self.my_slider.setTickPosition(QSlider.TicksAbove)
        self.my_slider.setTickInterval(10)
        self.my_slider.valueChanged.connect(self.get_value)
        
        self.my_slider.setMaximum(100)
        self.my_slider.setMinimum(10)
        
        vertBox.addWidget(self.my_text)
        vertBox.addWidget(self.temp_text)
        vertBox.addWidget(self.my_slider)

        self.setLayout(vertBox)

    def get_value(self):
        self.temp_text.setText(str(self.my_slider.value()))
        self.my_text.setFont(QFont("Times", self.my_slider.value()))




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
