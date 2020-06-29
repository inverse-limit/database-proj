import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_cart import *
from ui.ui_confirm_order import *


class cart(QtWidgets.QWidget, Ui_cart):
    switch_confirm_order = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(cart, self).__init__(parent)
        self.setupUi(self)
        self.cart_content = None
        self.pushButton_clear.clicked.connect(self.clear_cart)
        self.pushButton_pay.clicked.connect(self.confirm_order)

    def refresh_cart(self, user_data):
        """
        TODO:在用户从主页点击购物车按钮会打开购物车界面并触发该函数
             会把home类的self.user_data传入，利用这个从数据库查询购物车填到表里
             并把购物车的内容存到self.cart_content里
             之后调用这个函数如果self.cart_content不为None的话就用这个不用搜索数据库了
             这里的self.cart_content在点击结算按钮时会传给确认订单页面，请注意confirm_orderl类相应的函数
        """
        self.tableWidget.insertRow(0)

    def modify_cart(self, book_data):
        pass

    def clear_cart(self):
        reply = QtWidgets.QMessageBox.question(self, '清空购物车','确认要清空吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
        # TODO:点击确认清空购物车按钮触发该函数，清空画面和数据库里相关购物车内容
            pass
        else:
            pass

    def confirm_order(self):
        if self.tableWidget.rowCount() == 0:
            QtWidgets.QMessageBox.about(self, '确认支付', '购物车里没有商品!')
        else:
            self.switch_confirm_order.emit()


class confirm_order(QDialog, Ui_confirm_order):

    def __init__(self, parent=None):
        super(confirm_order, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_accept.clicked.connect(self.accept)
        self.comboBox_address.activated[str].connect(self.get_address)

    def put_in_data(self, user_data, cart_content):
        """
        TODO:打开确认订单页面时自动触发该函数，利用user_data和购物车初始化界面时填入的cart_content把相应内容
             填到确认订单页面，可以把user_data存到self.user_data里，下面get_address函数拿地址可以用到
        """
        # self.textBrowser.setText() 地址栏初始化时默认填入地址1

    def get_address(self, text):
        if text == '地址1':
            # self.textBrowser.setText(...) 填入地址1
            self.textBrowser.setReadOnly(True)
        elif text == '地址2':
            # 填入地址2
            self.textBrowser.setReadOnly(True)
        else:
            self.textBrowser.setReadOnly(False)  # 选择其它地址，开放地址栏编辑权限

    def cancel(self):
        self.done(-1)

    def accept(self):
        """
        TODO:用户点击确认支付界面
        """