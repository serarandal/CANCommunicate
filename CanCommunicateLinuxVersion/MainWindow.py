# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Utility


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout_3.addWidget(self.pushButton3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton3_2, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_3.setObjectName("pushButton3_3")
        self.pushButton3_3.clicked.connect(self.b3)
        self.verticalLayout_3.addWidget(self.pushButton3_3)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow3"))
        self.pushButton3.setText(_translate("MainWindow3", "SendMessage"))
        self.pushButton3_2.setText(_translate("MainWindow3", "SetID_Data"))
        self.pushButton3_3.setText(_translate("MainWindows3","ChangeMode"))
    def b3(self):
        MainWindow2.show()
        MainWindow3.hide()

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout.addWidget(self.listView_2, 3, 0, 1, 1)
        self.pushButton2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_2.setObjectName("pushButton2_2")
        self.pushButton2_2.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton2_2, 4, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        self.pushButton2_2.setText(_translate("MainWindow2", "ChangeMode"))
        self.pushButton2.setText(_translate("MainWindow2", "SendMessage"))
    def b1(self):
        MainWindow3.show()
        MainWindow2.hide()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.model = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model)
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.b3)
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.b4)
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "ReadCan"))
        self.pushButton.setText(_translate("MainWindow", "ConnectCan"))
        self.pushButton_3.setText(_translate("MainWindow", "SendPreMadeMessage"))
        self.pushButton_4.setText(_translate("MainWindow", "SendManMessage"))

    def b1(self):
        print("Pulsado boton 1:")
        status = Utility.connectCan("500000")
        it = QtGui.QStandardItem(status)
        self.model.appendRow(it)
    def b2(self):
        print("Pulsado boton 2:")
        Utility.readCan()
    def b3(self):
        print("Pulsado boton 3:")
        MainWindow2.show()
    def b4(self):
        print("Pulsado boton 4:")
        MainWindow3.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui2 = Ui_MainWindow2()
    ui3 = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    ui2.setupUi(MainWindow2)
    ui3.setupUi(MainWindow3)
    MainWindow.show()
    sys.exit(app.exec_())
