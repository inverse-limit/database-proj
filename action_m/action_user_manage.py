import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_user_manage import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
import time


class user_manage(QtWidgets.QWidget, Ui_user_manage):
    switch_user_profile = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(user_manage, self).__init__(parent)
        self.setupUi(self)
        self.comboBox_vip_status.addItems(['全部','非会员','会员','作家用户'])
        self.pushButton_search.clicked.connect(self.search)
        self.dateEdit_date1.setDate(QDate.currentDate())
        self.dateEdit_date2.setDate(QDate.currentDate())

    def search(self):
        """
        TODO:点击查询按钮根据lineEdit_search radioButton_account radioButton_nickname
             dateEdit_date1 dateEdit_date2 combobox_vip_status
        """
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.tableWidget.insertRow(0)
        option = [self.lineEdit_search.text(), self.radioButton_account.isChecked(),
                  self.radioButton_nickname.isChecked(), str(self.dateEdit_date1.date().toPyDate()),
                  str(self.dateEdit_date2.date().toPyDate()), self.comboBox_vip_status.currentText()]
        self.row = self.database.m_user_manage_search(option)
        self.tableWidget.setRowCount(0)
        n = len(self.row)
        for i in range(0, n):
            self.tableWidget.insertRow(i)  # 插入一行
            item = QTableWidgetItem(self.row[i].u_account)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item)

            item = QTableWidgetItem(self.row[i].u_nickname)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item)

            item = QTableWidgetItem(self.row[i].u_telephone)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item)

            if self.row[i].vip_status is None:
                sta = '非会员'
            elif self.row[i].vip_status >= date :
                sta = '会员有效期至 ' + str(self.row[i].vip_status)
            else:
                sta = '非会员'
            item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item)

            item = QTableWidgetItem(str(self.row[i].u_re_time))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的user_id存到self.press_id里，然后切换到用户详情用这个填信息
        """
        self.user_id = self.row[row].u_id
        self.user_detail()

    def user_detail(self):
        self.switch_user_profile.emit()