import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
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

    def search(self):
        """
        TODO:根据界面上的date1和date2搜索相应时间段内的订单，放到画面上
        """

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:用户双击表格后自动调用该函数，row, column为双击位置的行列数
             利用这个把你想要的东西存到self.order_id里，book_id会传到action_view_cart_order即订单详情
             这里的order_id要和那边的put_in_data函数对应
        """
        self.order_id = 'I am order_id'
        self.switch_view.emit()