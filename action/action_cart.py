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
        self.pushButton_selectall.clicked.connect(self.selectall)

    def refresh_cart(self, cart_content):
        """
        TODO:在用户从主页点击购物车按钮会打开购物车界面并触发该函数
             会把home类的self.cart_content传入，先把它存到这里的self.cart_content然后利用这个从数据库查询购物车填到表里
             这里的self.cart_content在点击结算按钮时会传给确认订单页面，请注意confirm_order类相应的函数
        """
        self.tableWidget.setRowCount(0)  # 先清空界面
        # 插入例
        for row in range(2):
            self.tableWidget.insertRow(row)
            test = QtWidgets.QTableWidgetItem(cart_content)
            test.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            test.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)  # 书名行用这列
            test.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(row, 0, test)

            price = QtWidgets.QTableWidgetItem('4.4')
            price.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            price.setFlags(QtCore.Qt.ItemIsEnabled)  # 其它行用这列 不要加上ItemIsUserCheckable
            self.tableWidget.setItem(row,2,price)

            number = QtWidgets.QTableWidgetItem('2')
            number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(row,3,number)  # 数量行连ItemIsEnabled也不要加

            total = float(self.tableWidget.item(row,2).text()) * float(self.tableWidget.item(row,3).text())
            total_t = QtWidgets.QTableWidgetItem('%.2f' % total)
            total_t.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            total_t.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row,4,total_t)


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
                total = float(self.tableWidget.item(p_row, 2).text()) * float(self.tableWidget.item(p_row, 3).text())
                total_t = QtWidgets.QTableWidgetItem('%.2f' % total)
                total_t.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                total_t.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(p_row, 4, total_t)


    def selectall(self):
        if self.tableWidget.rowCount() == 0:
            pass
        else:
            isallchecked = 0
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
                    isallchecked += 1
                else:
                    self.tableWidget.item(row, 0).setCheckState(QtCore.Qt.Checked)
            if isallchecked == self.tableWidget.rowCount():
                for row in range(self.tableWidget.rowCount()):
                    self.tableWidget.item(row, 0).setCheckState(QtCore.Qt.Unchecked)

    def clear_cart(self):
        reply = QtWidgets.QMessageBox.question(self, '删除选中项','确认要删除吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
        # TODO:点击确认删除选中项(这个我下面已经写好了)，同时删除数据库内相应记录并且对self.cart_content做相应改动
        #      删除选中列总是出bug，暂时只提供删除全部行
            self.tableWidget.setRowCount(0)
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
        self.cart_content = None

    def put_in_data(self, user_data, cart_content):
        """
        TODO:打开确认订单页面时自动触发该函数，利用user_data和购物车初始化界面时填入的cart_content把相应内容
             填到确认订单页面，并把user_data存到self.user_data里，下面get_address函数拿地址可以用到
             把cart_content存到self.cart_content里
        """
        print(cart_content)
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
             并对self.cart_content做相应处理
        """
        QtWidgets.QMessageBox.information(self, '确认订单', '支付成功')
        self.switch_cart.emit()
