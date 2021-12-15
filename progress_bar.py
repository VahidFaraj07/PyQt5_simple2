import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 500)
        self.setWindowTitle('ProgressBar Widget')
        self.UI()
        self.show()

    def UI(self):
        ver_box = QVBoxLayout()
        hor_box = QHBoxLayout()
        self.progress_bar = QProgressBar()
        button_start = QPushButton('Start')
        button_stop = QPushButton('Stop')

        button_start.clicked.connect(self.startProgress)
        button_stop.clicked.connect(self.stopProgress)

        self.progress_time = QTimer()
        self.progress_time.setInterval(10)
        self.progress_time.timeout.connect(self.runProgress)

        ver_box.addWidget(self.progress_bar)
        ver_box.addLayout(hor_box)
        hor_box.addWidget(button_start)
        hor_box.addWidget(button_stop)
        self.setLayout(ver_box)

    def runProgress(self):
        global count
        count += 1
        self.progress_bar.setValue(count)
        if count == 100:
            self.progress_time.stop()

    def startProgress(self):
        self.progress_time.start()

    def stopProgress(self):
        self.progress_time.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
