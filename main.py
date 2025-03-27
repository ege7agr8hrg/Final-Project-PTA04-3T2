from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem, QTableWidget, QMessageBox
import sys
from PyQt6 import uic
import webbrowser , json
from UI_800Blackout.opiumopium import Ui_MainWindow
class opium(QMainWindow, Ui_MainWindow ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])
        self.add(self, ["None", "Samsung Z Fold6", "Samsung", "Phone", "$1200"])


class homenew(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadmusic()
        uic.loadUi("UI_800Blackout/HomePage.ui", self)
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
        uic.loadUi("UI_800Blackout/SignUp Max.ui", self)
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
        
        if password.text() != confirmPassword.text():
            confirmPassword.setFocus()
            return
        
        with open("accounts.txt", "a") as file:
            file.write(username.text() + ":" + password.text() + "\n")
        self.close()
        lg.show()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_800Blackout/Login.ui", self)
        self.btnlogin.clicked.connect(self.checkLogin)
        self.btnSignup.clicked.connect(self.showSignUp)
    def showSignUp(self):
        self.close()
        Su.show()



    def checkLogin(self):
        if self.txtuseremail.text() == "admin" and self.txtpassword.text () == "admin":
            ad.show()
            self.close()
        else:

            with open("account.txt", "r") as file:
                data = file.readlines()
                accounts = []
                for line in data:
                    line = line.replace("\n", "")
                    line = line.strip()
                    accounts.append(line)

            if (self.txtuseremail.text() + ":" +self.txtpassword.text()) in accounts:
                self.close()
                home2.show()
            else:
                self.txtuseremail.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold SemiConden\"; color:black; background-color:#e25d5f;border-radius: 10px")
                self.txtpassword.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold SemiConden\";color:black; background-color:#e25d5f; border-radius: 10px")
class homepage (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_800Blackout/Final.ui", self)
        x = None
        self.btnphone.clicked.connect(lambda _, item = x: self.showbuy(LinkBuy = "https://www.samsung.com/us/smartphones/galaxy-z-fold6/buy/galaxy-z-fold6-256gb-unlocked-sm-f956uakaxaa/"))
        self.btnphone.clicked.connect(lambda _, item = x: self.showbuy(LinkBuy = "https://www.samsung.com/us/smartphones/galaxy-z-fold6/buy/galaxy-z-fold6-256gb-unlocked-sm-f956uakaxaa/"))
        self.btnlaptopmini.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(2))
        self.btnphonemini_3.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btnlaptopmini_2.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(2))
        self.btnmenu.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(7))
        self.btnmenu_2.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(7))
        self.btnphonemini_4.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btnlaptop.clicked.connect(lambda _, item = x: self.showbuy(LinkBuy = "https://www.apple.com/shop/buy-mac/macbook-pro"))
        self.btnphonemini_6.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btntablet.clicked.connect(lambda _, item = x: self.showbuy(LinkBuy = "https://www.samsung.com/us/tablets/galaxy-tab-s10/buy/galaxy-tab-s10-ultra-256gb-moonstone-gray-wi-fi-sm-x920nzaaxar/"))
        self.btntabletmini.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(4))
        self.btnlaptopmini_3.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(2))
        self.btntabletmini_3.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(4))
        self.btntabletmini_2 .clicked.connect(lambda:self.stackedsigma.setCurrentIndex(4))
        # self.btnnext.clicked.connect(self.showphone2)
        # self.btnprevious.clicked.connect(self.showmenu)
        self.btns25.clicked.connect(lambda _, item = x: self.showbuy(LinkBuy = "http://samsung.com/vn/smartphones/galaxy-s25/buy/"))
        self.btnmenu_6.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(7))
        self.btnmenu_5.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(7))
        self.btnmenu_4.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(7))
        self.btnmenu_3.clicked.connect(lambda:self.stackedsigma.setCurrentIndex(7))
        self.btnboombox3.clicked.connect(lambda _, item = x: self.showbuy (LinkBuy = "https://www.jbl.com/bluetooth-speakers/BOOMBOX-3-.html") )
        self.btnlaptopmini_5.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(2))
        self.btntabletmini_5.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(4))
        self.btnphonemini_7.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btnlaptopmini_6.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(2))
        self.btntabletmini_6.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(4))
        self.btnphonemini_8.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btnspeakermini.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(6))
        self.btnzfold6_prado.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(3))
        self.btnS25_PRADO.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(5))
        self.btnmcbk_m4u.clicked.connect(lambda: self.stackedsigma.setCurrentIndex(2))
        self.btntabs10_s.clicked.connect(lambda: self.stackedsigma.setCurrent(4))
        self.stackedsigma.setCurrentIndex(7)



    def showbuy(self, LinkBuy):
        webbrowser.open(LinkBuy)






class adminpage (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_800Blackout/admin.ui", self)
        self.btnadd.clicked.connect(self.add_row)
        self.btndel.clicked.connect(self.del_row)
        self.btnedit.clicked.connect(self.edit_row)
        self.btnsave.clicked.connect(self.save_data)
        self.btndel.clicked.connect(self.save_data)
        self.load_data()



    def load_data(self):
        with open("DATA/test.json", "r") as file:
            data = json.load(file)
            self.tableWidget.setRowCount(0)
            for row in data:
                row_pos = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_pos)
                for col_index, key in enumerate(row):
                    self.tableWidget.setItem(row_pos, col_index, QTableWidgetItem(row[key]))

    def save_data(self):
        with open ("DATA/test.json", "w") as file:
            data = []
            for i in range(self.tableWidget.rowCount()):
                name = self.tableWidget.item(i,0).text()
                manufactor = self.tableWidget.item(i,1).text()
                type = self.tableWidget.item(i, 2).text()
                price = self.tableWidget.item(i, 3).text()


                data.append({"name": name, "manufactor" : manufactor, "type" : type, "price" : price})
            json.dump(data, file, indent = 4)


    def add_row(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0 , QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 1 , QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 2 , QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 3 , QTableWidgetItem("..."))
        # self.tableWidget.setItem(row_position, 4 , QTableWidgetItem("..."))
        # self.tableWidget.setItem(row_position, 5 , QTableWidgetItem("..."))

        self.save_data()

    def edit_row(self):
        current_row = self.tableWidget.currentRow()
        current_col = self.tableWidget.currentColumn()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Please add a row to edit")
            return
        self.tableWidget.setItem(current_row, current_col, QTableWidgetItem("Edited"))
        self.save_data()
    def del_row(self):
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "you know what to do")
            return
        self.tableWidget.removeRow(current_row)
        self.save_data()
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    lg = Login()
    Su = SignUp()
    ad = adminpage()
    # home = homedashboard()
    home2 = homepage()
    OP = opium()
    lg.show()
    app.exec()