import sys
from PyQt5 import QtWidgets
import time
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_cart import *
from ui.ui_confirm_order import *
import pyodbc


class cart(QtWidgets.QWidget, Ui_cart):
    switch_confirm_order = QtCore.pyqtSignal()
    switch_book_detail = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(cart, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0,4)
        self.tableWidget.setColumnWidth(1, 70)
        self.cart_content = None
        self.p_col = None
        self.p_row = None
        self.book_id = None
        self.pushButton_clear.clicked.connect(self.clear_cart)
        self.pushButton_pay.clicked.connect(self.confirm_order)
        self.pushButton_selectall.clicked.connect(self.selectall)
        self.tableWidget.viewport().installEventFilter(self)  # 点击空白处时解除spinbox
        self.checklist = 0
        self.single_price = 4
        self.num = 5
        self.total_row = 6

    def refresh_cart(self, user_data):
        """
        TODO:在用户从主页点击购物车按钮会打开购物车界面并触发该函数
             从数据库得到购物车信息，可调用user_data，然后按照以下的方法填到画面里，注意下面的注释
             将从数据库得到的数据存到self.cart_content，建议先看一下下面confirm_order类的注释，两个类的数据需要协调一下
        """
        self.tableWidget.setRowCount(0)  # 先清空界面
        self.vip = user_data[5]
        self.cart_content = self.database.cart_select(user_data[0], self.vip)
        # 插入例
        self.total_price = 0
        if self.cart_content:
            self.cart_id = []
            n = len(self.cart_content)
            for row in range(0, n):
                self.cart_id.append(self.cart_content[row].cart_id)
                # 书名
                item = QtWidgets.QTableWidgetItem('')
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(row, 0, item)

                if self.cart_content[row].graph:
                    path = self.cart_content[row].graph
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(row, 1, item)
                else:
                    path = './icon/no_cover.jpg'
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(row, 1, item)


                self.tableWidget.insertRow(row)
                test = QtWidgets.QTableWidgetItem(self.cart_content[row].book_name)
                test.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                test.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)  # 书名行用这几行添加，为了有勾选框
                test.setCheckState(QtCore.Qt.Checked)
                self.tableWidget.setItem(row, 2, test)

                # 作者
                author = QtWidgets.QTableWidgetItem(str(self.cart_content[row].author_name))
                author.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                author.setFlags(QtCore.Qt.ItemIsEnabled)  # 其它行用这列 不要加上ItemIsUserCheckable
                self.tableWidget.setItem(row, 3, author)

                # 价格
                price = QtWidgets.QTableWidgetItem(str(self.cart_content[row].pr))
                price.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                price.setFlags(QtCore.Qt.ItemIsEnabled)  # 其它行用这列 不要加上ItemIsUserCheckable
                self.tableWidget.setItem(row,4,price)

                # 数量
                number = QtWidgets.QTableWidgetItem(str(self.cart_content[row].number))
                number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(row,5,number)  # 数量行连ItemIsEnabled也不要加

               # 单项总价
                total = float(self.tableWidget.item(row,4).text()) * float(self.tableWidget.item(row,5).text())
                total_t = QtWidgets.QTableWidgetItem('%.2f' % total)
                total_t.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                total_t.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row,6,total_t)

                self.total_price += total
        self.price.setText('%.2f' % self.total_price)  # 设置画面总价

    def modify_change_num(self, row, num):
        """
        TODO:触发该函数表示当前第row行的数量改成了num，self.cart_content和数据库里做相应改动，如果num=0就删除记录
             下面大段代码之下还有一个comfirm_order的类要填
             图像界面不用管，我下面一堆已经写了
        """
        self.cart_content = self.database.cart_changenum(self.cart_id[row], num, self.vip)


    def show_book_detail(self, row):
        """
        TODO:用户双击第row行的时候会自动调用该函数并自动把row当作参数传进来
             需要利用把row对应的book_id存到self.book_id里面，然后 self.switch_book_detail.emit() 切换到图书详情页
             就和主页双击行打开详情页一样
        """
        self.book_id = self.database.cart_book_detail(self.cart_id[row]).book_id
        self.switch_book_detail.emit()

    def clear_cart(self):
        reply = QtWidgets.QMessageBox.question(self, '删除选中项','确认要删除吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            row_num = int(self.tableWidget.rowCount())
            for row in range(row_num):
                inverse_id = row_num -1 - row
                if self.tableWidget.item(inverse_id,self.checklist).checkState() == QtCore.Qt.Checked:
                    self.modify_change_num(inverse_id, 0)
                    self.tableWidget.removeRow(inverse_id)
        self.refresh_price()

    def confirm_order(self):
        if self.tableWidget.rowCount() == 0:
            QtWidgets.QMessageBox.about(self, '确认支付', '购物车里没有商品!')
        else:
            self.select_list = []
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row,self.checklist).checkState() == QtCore.Qt.Checked:
                    self.select_list.append(row)
            self.switch_confirm_order.emit()

    def get_price(self, row=None):
        if isinstance(row, int):
            return float(self.tableWidget.item(row, self.total_row).text())
        else:
            return float(self.price.text())

    def on_tableWidget_cellClicked(self, row, column):
        if column == self.checklist:
            self.refresh_price()
        elif column == self.num:
            num = QtWidgets.QSpinBox(self)
            num.setMaximum(99)
            current_num = int(self.tableWidget.item(row,column).text())
            num.setValue(current_num)
            num.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setCellWidget(row, column, num)
            self.p_row = row
            self.p_col = column
            num.valueChanged.connect(self.changeprice)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        if not column == self.num:
            self.show_book_detail(row)

    def on_tableWidget_currentCellChanged(self, row, column, p_row, p_column):
        p_item = self.tableWidget.cellWidget(p_row, p_column)
        if p_item:
            if p_column == self.num:
                number = p_item.value()
                self.tableWidget.removeCellWidget(p_row, p_column)
                number = QtWidgets.QTableWidgetItem(str(number))
                number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(p_row, p_column, number)
                self.p_row = None
                self.p_col = None

    def changeprice(self):
        num = self.tableWidget.cellWidget(self.p_row, self.num).value()
        if num > 0:
            current_total_row = float(num) * float(self.tableWidget.item(self.p_row,self.single_price).text())
            current_total_row = QtWidgets.QTableWidgetItem('%.2f' % current_total_row)
            current_total_row.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            current_total_row.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(self.p_row, self.total_row, current_total_row)
            self.modify_change_num(self.p_row, num)
        else:
            self.tableWidget.cellWidget(self.p_row, self.num).setValue(1)
            reply = QtWidgets.QMessageBox.question(self, '购物车','要删除该项吗',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.tableWidget.removeRow(self.p_row)
                self.modify_change_num(self.p_row, num)
        self.refresh_price()

    def eventFilter(self, source, event):  # 在点击表格空白处时解除spinbox
        if (event.type() == QtCore.QEvent.MouseButtonPress and
            source is self.tableWidget.viewport() and
            self.tableWidget.itemAt(event.pos()) is None):
            if self.p_col and self.p_col == self.num:
                p_item = self.tableWidget.cellWidget(self.p_row, self.p_col)
                number = p_item.value()
                self.tableWidget.removeCellWidget(self.p_row, self.p_col)
                number = QtWidgets.QTableWidgetItem(str(number))
                number.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(self.p_row, self.p_col, number)
            self.p_col = None
            self.p_row = None
        return QtWidgets.QWidget.eventFilter(self, source, event)

    def selectall(self):  # 全选，若已全选则全反选
        if self.tableWidget.rowCount() == 0:
            pass
        else:
            isallchecked = 0
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row, self.checklist).checkState() == QtCore.Qt.Checked:
                    isallchecked += 1
                else:
                    self.tableWidget.item(row, self.checklist).setCheckState(QtCore.Qt.Checked)
            if isallchecked == self.tableWidget.rowCount():
                for row in range(self.tableWidget.rowCount()):
                    self.tableWidget.item(row, self.checklist).setCheckState(QtCore.Qt.Unchecked)
        self.refresh_price()

    def refresh_price(self):
        price = 0
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, self.checklist).checkState() == QtCore.Qt.Checked:
                price += self.get_price(row)
        self.price.setText('%.2f' % price)

    def get_image_label(self, image):
        image_label = QtWidgets.QLabel()
        image_label.setText('')
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap(image)
        pixmap.scaled(50, 40, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        return image_label

class confirm_order(QDialog, Ui_confirm_order):
    switch_cart = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(confirm_order, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_accept.clicked.connect(self.accept)
        self.comboBox_address.activated[str].connect(self.get_address)
        self.cart_content = None

    def put_in_data(self, user_data, cart_content, select_list):
        """
        TODO:打开确认订单页面时自动触发该函数，利用user_data和cart_content和选中信息select_list把相应内容填到确认订单页面，
             这里的cart_content是上面购物车类点击结算按钮的时刻购物车类的self.cart_content
             而选中信息select_list是点击结算按钮时被选中的行的索引(第一行是0)，注意购物车里删掉一行那下面的索引都会-1，
             想办法把索引和购物车内容cart_content匹配起来，把被选中的那些图书信息保存到self.order_content里
             并把user_data存到self.user_data里，下面get_address函数拿地址可以用到
        """
        n = len(select_list)
        self.order_content = []
        for i in range(0,n):
            self.order_content.append(cart_content[select_list[i]])
        self.user_data = user_data
        self.u_account.setText(user_data[0])
        self.u_nickname.setText(user_data[1])
        self.u_telephone.setText(user_data[3])
        self.price.setText(self.total_price)
        self.textBrowser.setText(self.user_data[6])   # 地址栏初始化时默认填入地址1

    def get_address(self, text):
        """
        TODO:见下方注释
        """
        if text == '地址1':
            self.textBrowser.setText(self.user_data[6])
            self.textBrowser.setReadOnly(True)
        elif text == '地址2':
            self.textBrowser.setText(self.user_data[7])
            self.textBrowser.setReadOnly(True)
        else:
            self.textBrowser.setReadOnly(False)  # 选择其它地址，开放地址栏编辑权限

    def cancel(self):
        self.done(-1)

    def accept(self):
        """
        TODO:用户点击确认支付界面，利用self.user_data以及self.order_content把订单数据填到数据库里
             并对数据库购物车表进行相应处理，减去已支付的书的数量，其它self里的属性不用管了
        """
        name = self.database.isorder(self.order_content)
        if name:
            QtWidgets.QMessageBox.about(self, '提示', '书籍 《' + name + '》 没有足够的库存！')
        else:
            self.database.order_ok(self.user_data, self.order_content)
            QtWidgets.QMessageBox.information(self, '确认订单', '支付成功')
            self.switch_cart.emit()
