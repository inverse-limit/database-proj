# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_buy_vip.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buy_vip(object):
    def setupUi(self, buy_vip):
        buy_vip.setObjectName("buy_vip")
        buy_vip.resize(407, 219)
        self.label = QtWidgets.QLabel(buy_vip)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton_1 = QtWidgets.QRadioButton(buy_vip)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 100, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_5 = QtWidgets.QRadioButton(buy_vip)
        self.radioButton_5.setGeometry(QtCore.QRect(120, 100, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(buy_vip)
        self.radioButton_6.setGeometry(QtCore.QRect(210, 100, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_12 = QtWidgets.QRadioButton(buy_vip)
        self.radioButton_12.setGeometry(QtCore.QRect(310, 100, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.pushButton_accept = QtWidgets.QPushButton(buy_vip)
        self.pushButton_accept.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_cancel = QtWidgets.QPushButton(buy_vip)
        self.pushButton_cancel.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(buy_vip)
        QtCore.QMetaObject.connectSlotsByName(buy_vip)

    def retranslateUi(self, buy_vip):
        _translate = QtCore.QCoreApplication.translate
        buy_vip.setWindowTitle(_translate("buy_vip", "开通会员"))
        self.label.setText(_translate("buy_vip", "开通会员享受部分图书价格优惠"))
        self.radioButton_1.setText(_translate("buy_vip", "一个月"))
        self.radioButton_5.setText(_translate("buy_vip", "三个月"))
        self.radioButton_6.setText(_translate("buy_vip", "六个月"))
        self.radioButton_12.setText(_translate("buy_vip", "一年"))
        self.pushButton_accept.setText(_translate("buy_vip", "确认开通"))
        self.pushButton_cancel.setText(_translate("buy_vip", "取消"))
