# Form implementation generated from reading ui file 'UI.800Blackout/opiumopium.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 785)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 801, 701))
        self.stackedWidget.setStyleSheet("background-color: #7e718b")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.page)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 731, 551))
        self.scrollArea.setMinimumSize(QtCore.QSize(731, 551))
        self.scrollArea.setMaximumSize(QtCore.QSize(731, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(131, 191))
        self.frame.setMaximumSize(QtCore.QSize(131, 191))
        self.frame.setStyleSheet("border-radius : 10px;\n"
"background-color : rgb(181, 162, 199)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 35, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 35, 10))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 35, 10))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 140, 35, 10))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.widget.setStyleSheet("background-color: #7e718b")
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.c = 1
        self.r = 0

    def add (self, MainWindow, l:list):
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(131, 191))
        self.frame.setMaximumSize(QtCore.QSize(131, 191))
        self.frame.setStyleSheet("border-radius : 10px;\n"
"background-color : rgb(181, 162, 199)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 35, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 35, 10))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 35, 10))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 140, 35, 10))
        self.label_9.setObjectName("label_9")
        self.doichu(self, l[0], l[1], l[2], l[3],l[4])
        self.gridLayout.addWidget(self.frame, self.r, self.c, 1, 1)
        self.c += 1
        if self.c == 3:
            self.r += 1
            self.c = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Manufacturer"))
        self.label_4.setText(_translate("MainWindow", "Type"))
        self.label_9.setText(_translate("MainWindow", ""))

    def doichu(self, MainWindow, Image="Insert", Name = "Insert", Manufacturer = "Insert", Type = "None", Price = "Insert"):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", Image))
        self.label_2.setText(_translate("MainWindow", Name))
        self.label_3.setText(_translate("MainWindow", Manufacturer))
        self.label_4.setText(_translate("MainWindow", Type))
        self.label_9.setText(_translate("MainWindow", Price))

