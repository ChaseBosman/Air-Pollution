from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window:
    def __init__(self):
        self.carbon_app = QApplication(sys.argv)
        self.carbon_window = QMainWindow()
        self.carbon_window.setGeometry(200, 200, 500, 300,)
        self.carbon_window.setWindowTitle("Current pollution levels")
        self.carbon_window.show()
        sys.exit(self.carbon_app.exec_())


if __name__ == "__main__":
    window = Window()
