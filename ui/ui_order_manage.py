# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_order_manage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_order_manage(object):
    def setupUi(self, order_manage):
        order_manage.setObjectName("order_manage")
        order_manage.resize(828, 545)
        self.gridLayout = QtWidgets.QGridLayout(order_manage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(order_manage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_search = QtWidgets.QLineEdit(order_manage)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 1, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(order_manage)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 2, 1, 1)
        self.radioButton_account = QtWidgets.QRadioButton(order_manage)
        self.radioButton_account.setChecked(True)
        self.radioButton_account.setObjectName("radioButton_account")
        self.gridLayout.addWidget(self.radioButton_account, 0, 3, 1, 1)
        self.radioButton_nickname = QtWidgets.QRadioButton(order_manage)
        self.radioButton_nickname.setObjectName("radioButton_nickname")
        self.gridLayout.addWidget(self.radioButton_nickname, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(order_manage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)
        self.dateEdit_date1 = QtWidgets.QDateEdit(order_manage)
        self.dateEdit_date1.setObjectName("dateEdit_date1")
        self.gridLayout.addWidget(self.dateEdit_date1, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(order_manage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 7, 1, 1)
        self.dateEdit_date2 = QtWidgets.QDateEdit(order_manage)
        self.dateEdit_date2.setObjectName("dateEdit_date2")
        self.gridLayout.addWidget(self.dateEdit_date2, 0, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 9, 1, 1)
        self.pushButton_stat = QtWidgets.QPushButton(order_manage)
        self.pushButton_stat.setObjectName("pushButton_stat")
        self.gridLayout.addWidget(self.pushButton_stat, 0, 10, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(order_manage)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 11)

        self.retranslateUi(order_manage)
        QtCore.QMetaObject.connectSlotsByName(order_manage)

    def retranslateUi(self, order_manage):
        _translate = QtCore.QCoreApplication.translate
        order_manage.setWindowTitle(_translate("order_manage", "订单管理"))
        self.label_3.setText(_translate("order_manage", "用户："))
        self.pushButton_search.setText(_translate("order_manage", "查询"))
        self.radioButton_account.setText(_translate("order_manage", "按用户名"))
        self.radioButton_nickname.setText(_translate("order_manage", "按昵称"))
        self.label.setText(_translate("order_manage", "时间："))
        self.label_2.setText(_translate("order_manage", "-"))
        self.pushButton_stat.setText(_translate("order_manage", "统计"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("order_manage", "提交时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("order_manage", "总价"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("order_manage", "用户"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("order_manage", "昵称"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("order_manage", "内容"))
