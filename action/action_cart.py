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
             这里的self.cart_content在点击结算按钮时会传给确认订单页面，请注意confirm_order类相应的函数
        """
        # 插入例
        for row in range(2):
            self.tableWidget.insertRow(row)
            test = QtWidgets.QTableWidgetItem('季')
            test.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            test.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)  # 书名行用这列
            test.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(row, 0, test)

            price = QtWidgets.QTableWidgetItem('4')
            test.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            test.setFlags(QtCore.Qt.ItemIsEnabled)  # 其它行用这列 不要加上ItemIsUserCheckable

            number = QtWidgets.QTableWidgetItem('2')
            number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(row,3,number)


    def on_tableWidget_cellDoubleClicked(self, row, column):
        if column == 3:
            num = QtWidgets.QSpinBox()
            num.setMaximum(99)
            current_num = int(self.tableWidget.item(row,column).text())
            num.setValue(current_num)
            num.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setCellWidget(row, column, num)
        else:
            pass

    def on_tableWidget_currentCellChanged(self, row, column, p_row, p_column):
        p_item = self.tableWidget.cellWidget(p_row, p_column)
        if p_item:
            if p_column == 3:
                number = p_item.value()
                self.tableWidget.removeCellWidget(p_row, p_column)
                number = QtWidgets.QTableWidgetItem(str(number))
                number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(p_row, p_column, number)

    def modify_cart(self, book_data):
        pass

    def clear_cart(self):
        reply = QtWidgets.QMessageBox.question(self, '清空购物车','确认要清空吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
        # TODO:点击确认清空购物车按钮触发该函数，清空画面和数据库里相关购物车内容
            self.tableWidget.setRowCount(0)
            self.price.setText('0')
        else:
            pass

    def confirm_order(self):
        if self.tableWidget.rowCount() == 0:
            QtWidgets.QMessageBox.about(self, '确认支付', '购物车里没有商品!')
        else:
            self.switch_confirm_order.emit()


class confirm_order(QDialog, Ui_confirm_order):
    switch_cart = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(confirm_order, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_accept.clicked.connect(self.accept)
        self.comboBox_address.activated[str].connect(self.get_address)

    def put_in_data(self, user_data, cart_content):
        """
        TODO:打开确认订单页面时自动触发该函数，利用user_data和购物车初始化界面时填入的cart_content把相应内容
             填到确认订单页面，并把user_data存到self.user_data里，下面get_address函数拿地址可以用到
             也把cart_content存到self.cart_content里
        """
        # self.textBrowser.setText() 地址栏初始化时默认填入地址1

    def get_address(self, text):
        """
        TODO:见下方注释
        """
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
        TODO:用户点击确认支付界面，利用self.user_data以及self.cart_content把订单数据填到数据库里
             并清空购物车
        """
        QtWidgets.QMessageBox.information(self, '确认订单', '支付成功')
