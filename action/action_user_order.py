import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_user_order import *


class user_order(QtWidgets.QWidget, Ui_user_order):
    switch_view = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(user_order, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_search.clicked.connect(self.search)
        self.order_id = None

    def put_in_data(self, user_data):
        """
        TODO:利用user_data调出历史订单信息放入界面，表格内容和管理界面的订单管理完全一样
        """
        [self.row, self.sell_id] = self.database.his_order(user_data[0], 'no', self.dateEdit_date1.date().toPyDate(),
                                                           self.dateEdit_date2.date().toPyDate())
        m = len(self.row)
        n = len(self.sell_id)
        text = ''
        self.account = user_data[0]
        for i in range(0, n):
            for j in range(0, m):
                if self.row[j].sell_id == self.sell_id[i].sell_id:
                    text += '图书' + self.row[j].book_id + str(self.row[j].number) + '本；'
                    s_date = self.row[j].s_date
                    total = self.row[j].total_price
            self.tableWidget.insertRow(i)
            item0 = QTableWidgetItem(str(s_date))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item0)

            item0 = QTableWidgetItem(str(total))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item0)

            item0 = QTableWidgetItem(text)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item0)

    def search(self):
        """
        TODO:根据界面上的date1和date2搜索相应时间段内的订单，放到画面上
        """
        [self.row, self.sell_id] = self.database.his_order(self.account, 'yes', str(self.dateEdit_date1.date().toPyDate()),
                                                           str(self.dateEdit_date2.date().toPyDate()))
        m = len(self.row)
        n = len(self.sell_id)
        text = ''
        self.tableWidget.setRowCount(0)
        for i in range(0, n):
            for j in range(0, m):
                if self.row[j].sell_id == self.sell_id[i].sell_id:
                    text += '图书' + self.row[j].book_id + str(self.row[j].number) + '本；'
                    s_date = self.row[j].s_date
                    total = self.row[j].total_price
            self.tableWidget.insertRow(i)
            item0 = QTableWidgetItem(str(s_date))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item0)

            item0 = QTableWidgetItem(str(total))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item0)

            item0 = QTableWidgetItem(text)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item0)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:用户双击表格后自动调用该函数，row, column为双击位置的行列数
             利用这个把你想要的东西存到self.order_id里，book_id会传到action_view_cart_order即订单详情
             这里的order_id要和那边的put_in_data函数对应
        """
        self.order_id = self.sell_id[row]
        self.switch_view.emit()