#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import PreMadeWindow
import Utility

class Popup6(object): #UI class
    def setupUi(self, PopupWindow6):
        PopupWindow6.setObjectName("Form")
        PopupWindow6.resize(400, 300)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow6)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow6)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow6)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form", "Popup2"))
        self.label.setText(_translate("Form", "Error al guardar el nuevo mensaje"))

class Popup5(object): #UI class
    def setupUi(self, PopupWindow5):
        PopupWindow5.setObjectName("Form")
        PopupWindow5.resize(400, 300)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow5)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow5)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow5)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow5)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup1"))
        self.label.setText(_translate("Form", "Nuevo mensaje Guardado"))

class Ui_MainWindow5(object): #UI class
    def setupUi(self,MainWindow5,ui2,PopupWindow5,PopupWindow6):
        self.Popup = PopupWindow5
        self.ui2 = ui2
        self.Popup2 = PopupWindow6
        self.MainWindow5 = MainWindow5
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        MainWindow5.setObjectName("MainWindow5")
        MainWindow5.resize(800,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow5)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20,40,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem,3,2,1,1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit,2,2,1,1)
        self.pushButton5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5_2.setObjectName("pushButton5_2")
        self.pushButton5_2.clicked.connect(self.saveNewMessagesButton)
        self.pushButton5_2.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton5_2,2,3,1,1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        MainWindow5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow5)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,22))
        self.menubar.setObjectName("menubar")
        MainWindow5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow5)
        self.statusbar.setObjectName("statusbar")
        MainWindow5.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow5)

    def saveNewMessagesButton(self):
        name=self.lineEdit.text()
        print(name)
        print("Pushed add new message button:")
        save = Utility.createNewPreMadeMessage(name)
        if save == True:
            self.ui2.addItemsListView()
            self.MainWindow5.close()
            self.Popup.show()
        else:
            self.Popup2.show()

    def retranslateUi(self, MainWindow5):
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow5", "CreateNewMessage"))
        self.pushButton5_2.setText(_translate("MainWindow5", "Create"))
        self.label.setText(_translate("MainWindow5", "Add new name to this message"))
