# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cart.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cart(object):
    def setupUi(self, cart):
        cart.setObjectName("cart")
        cart.resize(740, 580)
        self.gridLayout = QtWidgets.QGridLayout(cart)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(cart)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(119)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(598, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_total_price = QtWidgets.QLabel(cart)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_total_price.setFont(font)
        self.label_total_price.setObjectName("label_total_price")
        self.gridLayout.addWidget(self.label_total_price, 1, 1, 1, 1)
        self.price = QtWidgets.QLabel(cart)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(598, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(cart)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 2, 1, 1, 1)
        self.pushButton_pay = QtWidgets.QPushButton(cart)
        self.pushButton_pay.setObjectName("pushButton_pay")
        self.gridLayout.addWidget(self.pushButton_pay, 2, 2, 1, 1)

        self.retranslateUi(cart)
        QtCore.QMetaObject.connectSlotsByName(cart)

    def retranslateUi(self, cart):
        _translate = QtCore.QCoreApplication.translate
        cart.setWindowTitle(_translate("cart", "购物车"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("cart", "ISBN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("cart", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("cart", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("cart", "单价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("cart", "数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("cart", "总价"))
        self.label_total_price.setText(_translate("cart", "总计："))
        self.price.setText(_translate("cart", "价格"))
        self.pushButton_clear.setText(_translate("cart", "清空购物车"))
        self.pushButton_pay.setText(_translate("cart", "结算"))
