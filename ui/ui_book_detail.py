# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_book_detail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_book_detail(object):
    def setupUi(self, book_detail):
        book_detail.setObjectName("book_detail")
        book_detail.resize(487, 502)
        self.label_intro = QtWidgets.QLabel(book_detail)
        self.label_intro.setGeometry(QtCore.QRect(10, 270, 36, 16))
        self.label_intro.setObjectName("label_intro")
        self.intro = QtWidgets.QTextBrowser(book_detail)
        self.intro.setGeometry(QtCore.QRect(10, 300, 461, 111))
        self.intro.setObjectName("intro")
        self.layoutWidget = QtWidgets.QWidget(book_detail)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 460, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_add2cart = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_add2cart.setObjectName("pushButton_add2cart")
        self.horizontalLayout_6.addWidget(self.pushButton_add2cart)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_6.addWidget(self.pushButton_cancel)
        self.cover = QtWidgets.QLabel(book_detail)
        self.cover.setGeometry(QtCore.QRect(43, 31, 161, 211))
        self.cover.setText("")
        self.cover.setPixmap(QtGui.QPixmap("../icon/background.jpg"))
        self.cover.setScaledContents(True)
        self.cover.setObjectName("cover")
        self.widget = QtWidgets.QWidget(book_detail)
        self.widget.setGeometry(QtCore.QRect(251, 20, 211, 241))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_book_name = QtWidgets.QLabel(self.widget)
        self.label_book_name.setObjectName("label_book_name")
        self.gridLayout.addWidget(self.label_book_name, 0, 0, 1, 1)
        self.book_name = QtWidgets.QLabel(self.widget)
        self.book_name.setObjectName("book_name")
        self.gridLayout.addWidget(self.book_name, 0, 1, 1, 1)
        self.label_author = QtWidgets.QLabel(self.widget)
        self.label_author.setObjectName("label_author")
        self.gridLayout.addWidget(self.label_author, 1, 0, 1, 1)
        self.author = QtWidgets.QLabel(self.widget)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 1, 1, 1, 1)
        self.label_ISBN = QtWidgets.QLabel(self.widget)
        self.label_ISBN.setObjectName("label_ISBN")
        self.gridLayout.addWidget(self.label_ISBN, 2, 0, 1, 1)
        self.ISBN = QtWidgets.QLabel(self.widget)
        self.ISBN.setObjectName("ISBN")
        self.gridLayout.addWidget(self.ISBN, 2, 1, 1, 1)
        self.label_press = QtWidgets.QLabel(self.widget)
        self.label_press.setObjectName("label_press")
        self.gridLayout.addWidget(self.label_press, 3, 0, 1, 1)
        self.press = QtWidgets.QLabel(self.widget)
        self.press.setObjectName("press")
        self.gridLayout.addWidget(self.press, 3, 1, 1, 1)
        self.label_pressdata = QtWidgets.QLabel(self.widget)
        self.label_pressdata.setObjectName("label_pressdata")
        self.gridLayout.addWidget(self.label_pressdata, 4, 0, 1, 1)
        self.pressdate = QtWidgets.QLabel(self.widget)
        self.pressdate.setObjectName("pressdate")
        self.gridLayout.addWidget(self.pressdate, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.version = QtWidgets.QLabel(self.widget)
        self.version.setObjectName("version")
        self.gridLayout.addWidget(self.version, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.stock = QtWidgets.QLabel(self.widget)
        self.stock.setObjectName("stock")
        self.gridLayout.addWidget(self.stock, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.price = QtWidgets.QLabel(self.widget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 7, 1, 1, 1)

        self.retranslateUi(book_detail)
        QtCore.QMetaObject.connectSlotsByName(book_detail)

    def retranslateUi(self, book_detail):
        _translate = QtCore.QCoreApplication.translate
        book_detail.setWindowTitle(_translate("book_detail", "详细信息"))
        self.label_intro.setText(_translate("book_detail", "简介："))
        self.pushButton_add2cart.setText(_translate("book_detail", "加入购物车"))
        self.pushButton_cancel.setText(_translate("book_detail", "取消"))
        self.label_book_name.setText(_translate("book_detail", "书名："))
        self.book_name.setText(_translate("book_detail", "书名"))
        self.label_author.setText(_translate("book_detail", "作者/译者："))
        self.author.setText(_translate("book_detail", "作者/译者"))
        self.label_ISBN.setText(_translate("book_detail", "ISBN："))
        self.ISBN.setText(_translate("book_detail", "ISBN"))
        self.label_press.setText(_translate("book_detail", "出版社："))
        self.press.setText(_translate("book_detail", "出版社"))
        self.label_pressdata.setText(_translate("book_detail", "出版日期："))
        self.pressdate.setText(_translate("book_detail", "出版日期"))
        self.label.setText(_translate("book_detail", "版本号："))
        self.version.setText(_translate("book_detail", "版本号"))
        self.label_3.setText(_translate("book_detail", "库存："))
        self.stock.setText(_translate("book_detail", "库存"))
        self.label_5.setText(_translate("book_detail", "单价："))
        self.price.setText(_translate("book_detail", "单价"))
