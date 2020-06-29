import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_book_detail import *


class book_detail(QtWidgets.QWidget, Ui_book_detail):
    switch_cart = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(book_detail, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_add2cart.clicked.connect(self.add_to_cart)
        self.pushButton_cancel.clicked.connect(self.close)
        self.cart_content = None

    def put_in_data(self, book_id):
        """
        TODO:利用book_id调出图书信息，填到界面里，并且存到self.book_id里
        """
        print(book_id)

    def add_to_cart(self):
        """
        TODO:点击加入购物车触发该函数，需要把当前书的信息加入购物车信息之中
        """
        reply = QtWidgets.QMessageBox.question(self, '加入购物车', '是否要加入购物车',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            """
            TODO:这里利用self.cart_content，它是开启该界面自动传入的当前购物车信息，初始也就是之前购物车没加过东西为None
                 用你想要的格式把这个窗口书的信息加到self.cart_content里面，格式保持一致，购物车界面初始化填数据函数就是
                 调用这个self.cart_content
                 弄好了后self.switch_cart.emit()
            """
            self.switch_cart.emit()
        if reply == QtWidgets.QMessageBox.No:
            pass