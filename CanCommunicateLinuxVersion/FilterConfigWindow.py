# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterConfigWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1683, 1080)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Name_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name_label.sizePolicy().hasHeightForWidth())
        self.Name_label.setSizePolicy(sizePolicy)
        self.Name_label.setMinimumSize(QtCore.QSize(50, 50))
        self.Name_label.setMaximumSize(QtCore.QSize(50, 50))
        self.Name_label.setObjectName("Name_label")
        self.verticalLayout.addWidget(self.Name_label)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit_2.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id_label = QtWidgets.QLabel(Dialog)
        self.id_label.setMinimumSize(QtCore.QSize(50, 50))
        self.id_label.setMaximumSize(QtCore.QSize(50, 50))
        self.id_label.setObjectName("id_label")
        self.verticalLayout_2.addWidget(self.id_label)
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit_3.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_2.addWidget(self.textEdit_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bytes_label = QtWidgets.QLabel(Dialog)
        self.bytes_label.setMinimumSize(QtCore.QSize(50, 50))
        self.bytes_label.setMaximumSize(QtCore.QSize(300, 50))
        self.bytes_label.setObjectName("bytes_label")
        self.verticalLayout_3.addWidget(self.bytes_label)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.operation_label = QtWidgets.QLabel(Dialog)
        self.operation_label.setMaximumSize(QtCore.QSize(200, 50))
        self.operation_label.setObjectName("operation_label")
        self.verticalLayout_4.addWidget(self.operation_label)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.offset_label = QtWidgets.QLabel(Dialog)
        self.offset_label.setMinimumSize(QtCore.QSize(50, 50))
        self.offset_label.setMaximumSize(QtCore.QSize(50, 50))
        self.offset_label.setObjectName("offset_label")
        self.verticalLayout_5.addWidget(self.offset_label)
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit_4.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_5.addWidget(self.textEdit_4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Name_label.setText(_translate("Dialog", "Name"))
        self.id_label.setText(_translate("Dialog", "Id"))
        self.bytes_label.setText(_translate("Dialog", "bytes please add them with one space"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "write it like this:2 3 4"))
        self.operation_label.setText(_translate("Dialog", "Operation, leave it blank if not needed"))
        self.offset_label.setText(_translate("Dialog", "Offset"))
        self.pushButton.setText(_translate("Dialog", "Save Configuration"))
