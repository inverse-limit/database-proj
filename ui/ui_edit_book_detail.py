# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_book_detail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_book_detail(object):
    def setupUi(self, edit_book_detail):
        edit_book_detail.setObjectName("edit_book_detail")
        edit_book_detail.resize(497, 502)
        self.graphicsView = QtWidgets.QGraphicsView(edit_book_detail)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 194, 249))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.label_intro = QtWidgets.QLabel(edit_book_detail)
        self.label_intro.setGeometry(QtCore.QRect(20, 280, 36, 16))
        self.label_intro.setObjectName("label_intro")
        self.intro = QtWidgets.QPlainTextEdit(edit_book_detail)
        self.intro.setGeometry(QtCore.QRect(20, 310, 451, 121))
        self.intro.setObjectName("intro")
        self.layoutWidget = QtWidgets.QWidget(edit_book_detail)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 10, 207, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_book_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_book_name.setObjectName("label_book_name")
        self.gridLayout.addWidget(self.label_book_name, 0, 0, 1, 1)
        self.lineEdit_book_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_book_name.setObjectName("lineEdit_book_name")
        self.gridLayout.addWidget(self.lineEdit_book_name, 0, 1, 1, 1)
        self.label_author = QtWidgets.QLabel(self.layoutWidget)
        self.label_author.setObjectName("label_author")
        self.gridLayout.addWidget(self.label_author, 1, 0, 1, 1)
        self.lineEdit_author = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.gridLayout.addWidget(self.lineEdit_author, 1, 1, 1, 1)
        self.label_press = QtWidgets.QLabel(self.layoutWidget)
        self.label_press.setObjectName("label_press")
        self.gridLayout.addWidget(self.label_press, 2, 0, 1, 1)
        self.lineEdit_press = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_press.setObjectName("lineEdit_press")
        self.gridLayout.addWidget(self.lineEdit_press, 2, 1, 1, 1)
        self.label_pressdata = QtWidgets.QLabel(self.layoutWidget)
        self.label_pressdata.setObjectName("label_pressdata")
        self.gridLayout.addWidget(self.label_pressdata, 3, 0, 1, 1)
        self.lineEdit_pressdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_pressdate.setObjectName("lineEdit_pressdate")
        self.gridLayout.addWidget(self.lineEdit_pressdate, 3, 1, 1, 1)
        self.label_ISBN = QtWidgets.QLabel(self.layoutWidget)
        self.label_ISBN.setObjectName("label_ISBN")
        self.gridLayout.addWidget(self.label_ISBN, 4, 0, 1, 1)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout.addWidget(self.lineEdit_ISBN, 4, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(edit_book_detail)
        self.layoutWidget1.setGeometry(QtCore.QRect(321, 471, 158, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.retranslateUi(edit_book_detail)
        QtCore.QMetaObject.connectSlotsByName(edit_book_detail)

    def retranslateUi(self, edit_book_detail):
        _translate = QtCore.QCoreApplication.translate
        edit_book_detail.setWindowTitle(_translate("edit_book_detail", "编辑图书"))
        self.label_intro.setText(_translate("edit_book_detail", "简介："))
        self.label_book_name.setText(_translate("edit_book_detail", "书名："))
        self.label_author.setText(_translate("edit_book_detail", "作者/译者："))
        self.label_press.setText(_translate("edit_book_detail", "出版社："))
        self.label_pressdata.setText(_translate("edit_book_detail", "出版日期："))
        self.label_ISBN.setText(_translate("edit_book_detail", "ISBN："))
        self.pushButton_save.setText(_translate("edit_book_detail", "保存"))
        self.pushButton_cancel.setText(_translate("edit_book_detail", "取消"))
