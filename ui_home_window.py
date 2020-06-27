# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_home_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home_window(object):
    def setupUi(self, home_window):
        home_window.setObjectName("home_window")
        home_window.resize(1200, 736)
        self.centralwidget = QtWidgets.QWidget(home_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.class_label = QtWidgets.QLabel(self.centralwidget)
        self.class_label.setObjectName("class_label")
        self.horizontalLayout.addWidget(self.class_label)
        self.comboBox_class1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_class1.setObjectName("comboBox_class1")
        self.horizontalLayout.addWidget(self.comboBox_class1)
        self.hypho_label = QtWidgets.QLabel(self.centralwidget)
        self.hypho_label.setObjectName("hypho_label")
        self.horizontalLayout.addWidget(self.hypho_label)
        self.comboBox_class2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_class2.setObjectName("comboBox_class2")
        self.horizontalLayout.addWidget(self.comboBox_class2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_2.addWidget(self.pushButton_search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_name = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_name.setChecked(True)
        self.radioButton_name.setObjectName("radioButton_name")
        self.horizontalLayout_3.addWidget(self.radioButton_name)
        self.radioButton_author = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_author.setObjectName("radioButton_author")
        self.horizontalLayout_3.addWidget(self.radioButton_author)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_detail_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detail_search.setObjectName("pushButton_detail_search")
        self.horizontalLayout_4.addWidget(self.pushButton_detail_search)
        spacerItem2 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_u_profile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_u_profile.setObjectName("pushButton_u_profile")
        self.horizontalLayout_5.addWidget(self.pushButton_u_profile)
        spacerItem3 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_cart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cart.setObjectName("pushButton_cart")
        self.horizontalLayout_6.addWidget(self.pushButton_cart)
        spacerItem4 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 388, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_contact = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_contact.setObjectName("pushButton_contact")
        self.horizontalLayout_7.addWidget(self.pushButton_contact)
        spacerItem6 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(117)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.lineEdit_pagejump = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pagejump.setObjectName("lineEdit_pagejump")
        self.horizontalLayout_8.addWidget(self.lineEdit_pagejump)
        self.pushButton_page_jump = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_page_jump.setObjectName("pushButton_page_jump")
        self.horizontalLayout_8.addWidget(self.pushButton_page_jump)
        self.label_current_page = QtWidgets.QLabel(self.centralwidget)
        self.label_current_page.setObjectName("label_current_page")
        self.horizontalLayout_8.addWidget(self.label_current_page)
        self.label_all_page = QtWidgets.QLabel(self.centralwidget)
        self.label_all_page.setObjectName("label_all_page")
        self.horizontalLayout_8.addWidget(self.label_all_page)
        self.pushButton_last_page = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_last_page.setObjectName("pushButton_last_page")
        self.horizontalLayout_8.addWidget(self.pushButton_last_page)
        self.pushButton_next_page = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next_page.setObjectName("pushButton_next_page")
        self.horizontalLayout_8.addWidget(self.pushButton_next_page)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        home_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(home_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        home_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(home_window)
        self.statusbar.setObjectName("statusbar")
        home_window.setStatusBar(self.statusbar)

        self.retranslateUi(home_window)
        QtCore.QMetaObject.connectSlotsByName(home_window)

    def retranslateUi(self, home_window):
        _translate = QtCore.QCoreApplication.translate
        home_window.setWindowTitle(_translate("home_window", "网上书店"))
        self.class_label.setText(_translate("home_window", "类别"))
        self.hypho_label.setText(_translate("home_window", "-"))
        self.pushButton_search.setText(_translate("home_window", "搜索"))
        self.radioButton_name.setText(_translate("home_window", "按书名"))
        self.radioButton_author.setText(_translate("home_window", "按作者"))
        self.pushButton_detail_search.setText(_translate("home_window", "高级搜索"))
        self.pushButton_u_profile.setText(_translate("home_window", "用户信息"))
        self.pushButton_cart.setText(_translate("home_window", "购物车"))
        self.pushButton_contact.setText(_translate("home_window", "联系我们"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("home_window", "ISBN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("home_window", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("home_window", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("home_window", "分类"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("home_window", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("home_window", "单价"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("home_window", "月销量"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("home_window", "库存"))
        self.pushButton_page_jump.setText(_translate("home_window", "跳转"))
        self.label_current_page.setText(_translate("home_window", "第 x 页"))
        self.label_all_page.setText(_translate("home_window", "共 x 页"))
        self.pushButton_last_page.setText(_translate("home_window", "上一页"))
        self.pushButton_next_page.setText(_translate("home_window", "下一页"))
