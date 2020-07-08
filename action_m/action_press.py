import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_press import *


class press(QtWidgets.QWidget, Ui_press):
    switch_detail_press = QtCore.pyqtSignal()
    switch_add = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(press, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_add_press.clicked.connect(self.switch_add_window)

    def search(self):
        """
        TODO:点击查询按钮进行搜索，搜索条件有框里的字和radioButton_press_name和radioButton_person
        """
        self.tableWidget.setRowCount(0)
        option = [self.lineEdit_search.text(), self.radioButton_press_name.isChecked(), self.radioButton_person.isChecked()]
        self.row = self.database.m_press_search(option)
        if self.row:
            n = len(self.row)
            for i in range(0,n):
                self.tableWidget.insertRow(i)
                item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 0, item)

                item = QTableWidgetItem(self.row[i].person)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 1, item)

                item = QTableWidgetItem(str(self.row[i].telephone))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 2, item)

                item = QTableWidgetItem(self.row[i].email)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 3, item)

                item = QTableWidgetItem(self.row[i].address)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i, 4, item)
        else:
            pass

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的press_id存到self.press_id里，然后切换到出版社详情用这个填信息
        """
        self.press_id = self.row[row].press_id
        self.press_detail()

    def switch_add_window(self):
        self.switch_add.emit()

    def press_detail(self):
        self.switch_detail_press.emit()