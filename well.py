from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys
import webbrowser

class homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI .800 Blackout/whateverthisis.ui", self)
        self.starternote.clicked.connect(self.showPage1)
    def showPage1(self):
        self.stacksigma.setCurrentIndex(1)
if __name__=="__main__":
    app = QApplication(sys.argv)
    home = homepage()
    home.show()
    app.exec()