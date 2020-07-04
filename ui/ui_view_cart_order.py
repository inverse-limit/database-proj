# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view_cart_order.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_view_cart_order(object):
    def setupUi(self, view_cart_order):
        view_cart_order.setObjectName("view_cart_order")
        view_cart_order.resize(690, 542)
        self.gridLayout = QtWidgets.QGridLayout(view_cart_order)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(view_cart_order)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_nickname = QtWidgets.QLabel(view_cart_order)
        self.label_nickname.setObjectName("label_nickname")
        self.gridLayout.addWidget(self.label_nickname, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(view_cart_order)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(view_cart_order)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.label_account = QtWidgets.QLabel(view_cart_order)
        self.label_account.setObjectName("label_account")
        self.gridLayout.addWidget(self.label_account, 0, 1, 1, 1)
        self.label_total = QtWidgets.QLabel(view_cart_order)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 0, 7, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(view_cart_order)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(90)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 8)

        self.retranslateUi(view_cart_order)
        QtCore.QMetaObject.connectSlotsByName(view_cart_order)

    def retranslateUi(self, view_cart_order):
        _translate = QtCore.QCoreApplication.translate
        view_cart_order.setWindowTitle(_translate("view_cart_order", "购物信息"))
        self.label_3.setText(_translate("view_cart_order", "昵称："))
        self.label_nickname.setText(_translate("view_cart_order", "昵称"))
        self.label.setText(_translate("view_cart_order", "用户："))
        self.label_5.setText(_translate("view_cart_order", "总计："))
        self.label_account.setText(_translate("view_cart_order", "用户名"))
        self.label_total.setText(_translate("view_cart_order", "总计"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("view_cart_order", "封面"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("view_cart_order", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("view_cart_order", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("view_cart_order", "单价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("view_cart_order", "数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("view_cart_order", "总价"))
