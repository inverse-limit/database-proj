import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
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

    def search(self):
        """
        TODO:点击查询按钮根据lineEdit_search radioButton_account radioButton_nickname
             dateEdit_date1 dateEdit_date2 查询订单 按时间顺序排序最近的排在上面
        """
        self.tableWidget.insertRow(0)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的order_id存到self.order_id里，然后切换到订单详情用这个填信息
        """
        self.order_id = 'I am order_id'
        self.switch_order_detail.emit()

    def stat(self):
        """
        TODO:看一下action_stat界面里的函数，把那边需要的数据存到self.data里，它会自动传到action_stat里
        """
        self.data = None
        self.switch_stat.emit()