# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_press.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_press(object):
    def setupUi(self, press):
        press.setObjectName("press")
        press.resize(1025, 566)
        self.gridLayout = QtWidgets.QGridLayout(press)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_search = QtWidgets.QLineEdit(press)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(press)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 1, 1, 1)
        self.radioButton_press_name = QtWidgets.QRadioButton(press)
        self.radioButton_press_name.setChecked(True)
        self.radioButton_press_name.setObjectName("radioButton_press_name")
        self.gridLayout.addWidget(self.radioButton_press_name, 0, 2, 1, 1)
        self.radioButton_person = QtWidgets.QRadioButton(press)
        self.radioButton_person.setObjectName("radioButton_person")
        self.gridLayout.addWidget(self.radioButton_person, 0, 3, 1, 1)
        self.pushButton_add_press = QtWidgets.QPushButton(press)
        self.pushButton_add_press.setObjectName("pushButton_add_press")
        self.gridLayout.addWidget(self.pushButton_add_press, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(468, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(press)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 6)

        self.retranslateUi(press)
        QtCore.QMetaObject.connectSlotsByName(press)

    def retranslateUi(self, press):
        _translate = QtCore.QCoreApplication.translate
        press.setWindowTitle(_translate("press", "出版社管理"))
        self.pushButton_search.setText(_translate("press", "搜索出版社"))
        self.radioButton_press_name.setText(_translate("press", "按名称"))
        self.radioButton_person.setText(_translate("press", "按联系人"))
        self.pushButton_add_press.setText(_translate("press", "添加出版社"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("press", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("press", "联系人"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("press", "电话"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("press", "邮箱"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("press", "地址"))
