import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from ui.ui_order_manage import *


class order_manage(QtWidgets.QWidget, Ui_order_manage):
    switch_order_detail = QtCore.pyqtSignal()
    switch_stat = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(order_manage, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_stat.clicked.connect(self.stat)
        self.order_id = 'order_id'  # 测试
        self.dateEdit_date1.setDate(QDate.currentDate())
        self.dateEdit_date2.setDate(QDate.currentDate())

    def search(self):
        """
        TODO:点击查询按钮根据lineEdit_search radioButton_account radioButton_nickname
             dateEdit_date1 dateEdit_date2 查询订单 按时间顺序排序最近的排在上面
        """
        self.tableWidget.setRowCount(0)
        option = [self.lineEdit_search.text(), self.radioButton_account.isChecked(),
                  self.radioButton_nickname.isChecked(), str(self.dateEdit_date1.date().toPyDate()),
                  str(self.dateEdit_date2.date().toPyDate())]
        [self.row, self.sell_id] = self.database.m_order_manage_search(option)
        m = len(self.row)
        n = len(self.sell_id)
        for i in range(0,n):
            text = ''
            for j in range(0,m):
                if self.row[j].sell_id == self.sell_id[i].sell_id:
                    text += '图书 《' + self.row[j].book_name + '》 ' + str(self.row[j].number) + '本；'
                    s_date = self.row[j].s_date
                    total = self.row[j].total_price
                    account = self.row[j].u_account
                    nickname = self.row[j].u_nickname
            self.tableWidget.insertRow(i)
            item0 = QTableWidgetItem(str(s_date))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item0)

            item0 = QTableWidgetItem(str(total))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item0)

            item0 = QTableWidgetItem(account)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item0)

            item0 = QTableWidgetItem(nickname)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item0)

            item0 = QTableWidgetItem(text)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item0)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的order_id存到self.order_id里，然后切换到订单详情用这个填信息
        """
        self.order_id = self.sell_id[row]
        self.switch_order_detail.emit()


    def stat(self):
        """
        TODO:看一下action_stat界面里的函数，把那边需要的数据存到self.data里，它会自动传到action_stat里
        """
        self.data = (str(self.dateEdit_date1.date().toPyDate()), str(self.dateEdit_date2.date().toPyDate()))
        self.switch_stat.emit()
