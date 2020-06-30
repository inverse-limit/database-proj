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
        TODO:利用book_id(见action_home_window on_tableWidget_cellDoubleClicked)调出图书信息，
             填到界面里，并且存到self.book_id里
        """

    def add_to_cart(self):
        reply = QtWidgets.QMessageBox.question(self, '加入购物车', '是否要加入购物车',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            # TODO: 同意加入购物车触发该函数，把页面里书的信息（利用self.book_id）加到数据库购物车表里，
            #  用户信息可由self.user_data调用，就是home类的那个
            self.switch_cart.emit()  # 这行放最下面
        if reply == QtWidgets.QMessageBox.No:
            pass