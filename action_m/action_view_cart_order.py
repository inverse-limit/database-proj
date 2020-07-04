import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_view_cart_order import *


class view_cart_order(QtWidgets.QWidget, Ui_view_cart_order):
    switch_book = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(view_cart_order, self).__init__(parent)
        self.setupUi(self)

    def put_in_user_data(self, user_id=None, order_id=None):
        """
        TODO:这个界面在用户信息查看订单/购物车按钮按下后打开
             利用传入的user_id或order_id填label_account(用户名)和label_nickname(昵称)
        """
        if user_id:
            # TODO:用user_id搜出该用户购物车信息填到表里
            pass
        else:
            # TODO:用order_id相应的订单信息填到表里
            print(order_id)
        # 最后把总价填到label_total里

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:把book_id整到self里
        """
        self.book_id = 'I come from home'
        self.switch_book.emit()

