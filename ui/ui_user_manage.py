# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user_manage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_manage(object):
    def setupUi(self, user_manage):
        user_manage.setObjectName("user_manage")
        user_manage.resize(825, 554)
        self.gridLayout = QtWidgets.QGridLayout(user_manage)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_search = QtWidgets.QLineEdit(user_manage)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(user_manage)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 1, 1, 1)
        self.radioButton_account = QtWidgets.QRadioButton(user_manage)
        self.radioButton_account.setChecked(True)
        self.radioButton_account.setObjectName("radioButton_account")
        self.gridLayout.addWidget(self.radioButton_account, 0, 2, 1, 1)
        self.radioButton_nickname = QtWidgets.QRadioButton(user_manage)
        self.radioButton_nickname.setObjectName("radioButton_nickname")
        self.gridLayout.addWidget(self.radioButton_nickname, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(user_manage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.dateEdit_date1 = QtWidgets.QDateEdit(user_manage)
        self.dateEdit_date1.setObjectName("dateEdit_date1")
        self.gridLayout.addWidget(self.dateEdit_date1, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(user_manage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.dateEdit_date2 = QtWidgets.QDateEdit(user_manage)
        self.dateEdit_date2.setObjectName("dateEdit_date2")
        self.gridLayout.addWidget(self.dateEdit_date2, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(user_manage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 8, 1, 1)
        self.comboBox_vip_status = QtWidgets.QComboBox(user_manage)
        self.comboBox_vip_status.setObjectName("comboBox_vip_status")
        self.gridLayout.addWidget(self.comboBox_vip_status, 0, 9, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(user_manage)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(161)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 10)

        self.retranslateUi(user_manage)
        QtCore.QMetaObject.connectSlotsByName(user_manage)

    def retranslateUi(self, user_manage):
        _translate = QtCore.QCoreApplication.translate
        user_manage.setWindowTitle(_translate("user_manage", "会员管理"))
        self.pushButton_search.setText(_translate("user_manage", "搜索用户"))
        self.radioButton_account.setText(_translate("user_manage", "按用户名"))
        self.radioButton_nickname.setText(_translate("user_manage", "按昵称"))
        self.label.setText(_translate("user_manage", "注册时间："))
        self.label_2.setText(_translate("user_manage", "-"))
        self.label_3.setText(_translate("user_manage", "会员状态："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("user_manage", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("user_manage", "昵称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("user_manage", "电话"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("user_manage", "会员状态"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("user_manage", "注册时间"))
