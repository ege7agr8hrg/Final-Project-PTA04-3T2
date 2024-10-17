from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys

class homedashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI .800 Blackout/HomePage.ui", self)
        self.btnHome.clicked.connect(self.showHome)

        self.btnProfile.clicked.connect(self.showProfile)
    def showHome(self):
        self.stackMenu.setCurrentIndex(1)
    def showProfile(self):
        self.stackedMenu.setCurrentIndex(2)
class SignUp(QMainWindow):
    def __init__(self):
        super(). __init__()
        uic.loadUi("UI .800 Blackout/SignUp Max.ui", self)
        self.btnSignUp.clicked.connect(self.registerAccount)
        self.btnLogin.clicked.connect(self.showLogin)
    def showLogin(self):
        self.close()
        lg.show()
    def registerAccount(self):
        username = self.txtUserName
        password = self.txtPassword
        confirmPassword = self.txtConfirmpassword
        if username.text() == "":
            username.setFocus()
            return
        if password.text () == "":
            password.setFocus()
            return
        
        if username.text() != confirmPassword.text():
            confirmPassword.setFocus()
            return
        
        with open("accounts.txt", "a") as file:
            file.write(username.text() + ":" + password.text() + "\n")
        self.close()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui .800 Blackout/Login.ui", self)
        self.btnlogin.clicked.connect(self.checkLogin)
        self.btnSignup.clicked.connect(self.showSignUp)
    def showSignUp(self):
        self.close()
        Su.show()



    def checkLogin(self):
        with open("account.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)

        if (self.txtuseremail.text() + ":" +self.txtpassword.text()) in accounts:
            self.close()
            home.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    lg = Login()
    Su = SignUp()
    home = homedashboard()
    lg.show()
    app.exec()