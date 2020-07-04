# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_press_detail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_press_detail(object):
    def setupUi(self, press_detail):
        press_detail.setObjectName("press_detail")
        press_detail.resize(449, 388)
        self.gridLayout = QtWidgets.QGridLayout(press_detail)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(press_detail)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.press_name = QtWidgets.QLineEdit(press_detail)
        self.press_name.setObjectName("press_name")
        self.gridLayout.addWidget(self.press_name, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(press_detail)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.person = QtWidgets.QLineEdit(press_detail)
        self.person.setObjectName("person")
        self.gridLayout.addWidget(self.person, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(press_detail)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.telephone = QtWidgets.QLineEdit(press_detail)
        self.telephone.setObjectName("telephone")
        self.gridLayout.addWidget(self.telephone, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(press_detail)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(press_detail)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(press_detail)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 3)
        self.address = QtWidgets.QPlainTextEdit(press_detail)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 5, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 2)
        self.pushButton_save = QtWidgets.QPushButton(press_detail)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 6, 2, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(press_detail)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 6, 3, 1, 1)

        self.retranslateUi(press_detail)
        QtCore.QMetaObject.connectSlotsByName(press_detail)

    def retranslateUi(self, press_detail):
        _translate = QtCore.QCoreApplication.translate
        press_detail.setWindowTitle(_translate("press_detail", "出版社"))
        self.label.setText(_translate("press_detail", "名称："))
        self.label_2.setText(_translate("press_detail", "联系人："))
        self.label_3.setText(_translate("press_detail", "电话："))
        self.label_4.setText(_translate("press_detail", "邮箱："))
        self.label_5.setText(_translate("press_detail", "地址："))
        self.pushButton_save.setText(_translate("press_detail", "保存"))
        self.pushButton_cancel.setText(_translate("press_detail", "取消"))
