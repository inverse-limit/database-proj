# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user_order.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_order(object):
    def setupUi(self, user_order):
        user_order.setObjectName("user_order")
        user_order.resize(827, 544)
        self.gridLayout = QtWidgets.QGridLayout(user_order)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(user_order)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit_date1 = QtWidgets.QDateEdit(user_order)
        self.dateEdit_date1.setObjectName("dateEdit_date1")
        self.gridLayout.addWidget(self.dateEdit_date1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(user_order)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.dateEdit_date2 = QtWidgets.QDateEdit(user_order)
        self.dateEdit_date2.setObjectName("dateEdit_date2")
        self.gridLayout.addWidget(self.dateEdit_date2, 0, 3, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(user_order)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(483, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(user_order)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 6)

        self.retranslateUi(user_order)
        QtCore.QMetaObject.connectSlotsByName(user_order)

    def retranslateUi(self, user_order):
        _translate = QtCore.QCoreApplication.translate
        user_order.setWindowTitle(_translate("user_order", "历史订单"))
        self.label.setText(_translate("user_order", "时间："))
        self.label_2.setText(_translate("user_order", "-"))
        self.pushButton_search.setText(_translate("user_order", "查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("user_order", "提交时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("user_order", "总价"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("user_order", "内容"))
