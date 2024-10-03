from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui .800 Blackout/Login.ui", self)
        self.btnlogin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        if self.txtuseremail.text() == "Skibiditoiletohiorizz" and self.txtpassword.text() == "123":
            self.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    lg = Login()
    lg.show()
    app.exec()