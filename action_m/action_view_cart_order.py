import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_view_cart_order import *


class view_cart_order(QtWidgets.QWidget, Ui_view_cart_order):
    switch_book = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(view_cart_order, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 80)

    def put_in_user_data(self, user_id=None, order_id=None):
        """
        TODO:这个界面在用户信息查看订单/购物车按钮按下后打开
             利用传入的user_id或order_id填label_account(用户名)和label_nickname(昵称)
        """
        if user_id:
            self.tableWidget.setRowCount(0)
            self.row = self.database.m_cart_view_u(user_id)
            n = len(self.row)
            total = 0
            for i in range(0,n):
                self.tableWidget.insertRow(i)
                self.label_account.setText(self.row[i].u_account)
                self.label_nickname.setText(self.row[i].u_nickname)

                path = './icon/test_pic2.jpg'
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 0, item)

                item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 1, item)

                item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 2, item)

                item = QTableWidgetItem(str(self.row[i].price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 3, item)

                item = QTableWidgetItem(str(self.row[i].number))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 4, item)

                item = QTableWidgetItem(str(self.row[i].price*self.row[i].number))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 5, item)

                total += self.row[i].price * self.row[i].number
            self.label_total.setText(str(total))
            # TODO:用user_id搜出该用户购物车信息填到表里
            # 第一列是图片
            # self.tableWidget.insertRow(0)
            # path = './icon/test_pic2.jpg'
            # item = self.get_image_label(path)
            # self.tableWidget.setCellWidget(0, 0, item)
        else:
            # TODO:用order_id相应的订单信息填到表里
            self.tableWidget.setRowCount(0)
            self.row = self.database.m_order_view(order_id)
            n = len(self.row)
            total = 0
            for i in range(0, n):
                self.tableWidget.insertRow(i)
                self.label_account.setText(self.row[i].u_account)
                self.label_nickname.setText(self.row[i].u_nickname)

                path = './icon/test_pic2.jpg'
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 0, item)

                item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 1, item)

                item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 2, item)

                item = QTableWidgetItem(str(self.row[i].price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 3, item)

                item = QTableWidgetItem(str(self.row[i].number))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 4, item)

                item = QTableWidgetItem(str(self.row[i].price * self.row[i].number))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 5, item)
            self.label_total.setText(str(total))
        # 最后把总价填到label_total里

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:把book_id整到self里
        """
        self.book_id = self.row[row].book_id
        self.switch_book.emit()

    def get_image_label(self, image):
        image_label = QtWidgets.QLabel()
        image_label.setText('')
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap(image)
        pixmap.scaled(50, 40, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        return image_label

