from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys
import webbrowser
class homedashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI .800 Blackout/HomePage.ui", self)
        self.btnHome.clicked.connect(self.showHome)
        x = None
        self.btnProfile.clicked.connect(self.showProfile)
        self.btnforallthedogs1.clicked.connect(self.showPage1)
        self.btnforallthedogs2.clicked.connect(self.showPage1)
        self.btnvirginiabeach.clicked.connect(lambda _, item = x: self.playmusic(LinkMusic = "https://open.spotify.com/track/3eP13S8D5m2cweMEg3ZDed?si=7c94dd05bff346e3"))
        self.btnamen_2.clicked.connect(lambda _, item = x: self.playmusic(LinkMusic = "https://open.spotify.com/track/0Mrnt1YqVuW2bqmwu4VxDt?si=74beb5a037d044cb"))
        self.btncallingforyou_2.clicked.connect(lambda _, item = x: self.playmusic(LinkMusic = "https://open.spotify.com/track/2nibvvDdAQkVraYP00z2RS?si=c6a4bb5619b94a8a"))
        self.btnfirstpersonshooter_2.clicked.connect(lambda _, item = x: self.playmusic(LinkMusic = "https://open.spotify.com/track/7aqfrAY2p9BUSiupwk3svU?si=e9f8e978ee0243ec"))                                      

    def playmusic(self, LinkMusic):
        webbrowser.open(LinkMusic)

    def showPage1(self):
        self.stackedMenu.setCurrentIndex(1)
    def showHome(self):
        self.stackedMenu.setCurrentIndex(0)
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