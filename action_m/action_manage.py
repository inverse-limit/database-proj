import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_manage import *


class manage(QtWidgets.QMainWindow, Ui_manage):
    switch_detail_research = QtCore.pyqtSignal()
    switch_book_detail = QtCore.pyqtSignal()
    switch_add_book = QtCore.pyqtSignal()
    switch_press = QtCore.pyqtSignal()
    switch_user = QtCore.pyqtSignal()
    switch_order = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(manage, self).__init__(parent)
        self.setupUi(self)
        # 跳转链接
        self.pushButton_detail_search.clicked.connect(self.detail_search_window)
        # 功能按钮
        self.pushButton_search.clicked.connect(self.simple_search)
        self.pushButton_last_page.clicked.connect(self.last_page)
        self.pushButton_next_page.clicked.connect(self.next_page)
        self.pushButton_page_jump.clicked.connect(self.page_jump)
        self.pushButton_add_book.clicked.connect(self.add_book)
        self.pushButton_press_manage.clicked.connect(self.show_press)
        self.pushButton_user_manage.clicked.connect(self.show_user)
        self.pushButton_order_manage.clicked.connect(self.show_order)
        self.pushButton_selectall.clicked.connect(self.selectall)
        self.pushButton_down.clicked.connect(self.down_book)
        self.pushButton_up.clicked.connect(self.up_book)
        self.pushButton_delete.clicked.connect(self.delete_book)

        self.comboBox_class1.activated[str].connect(self.get_class2)
        self.comboBox_class2.addItem('...')
        self.comboBox_filter.addItems(['已上架','未上架','全部'])
        self.comboBox_sort.addItems(['默认','销量降序','销量升序','价格降序','价格升序'])
        self.comboBox_filter.activated[str].connect(self.refresh_filter)
        self.comboBox_sort.activated[str].connect(self.refresh_sort)
        self.simple_research_option = None  # 简单查询条件
        self.detail_research_option = None  # 复杂查询条件

    def put_in_data(self):
        """
        TODO:和home一样
        """

    def get_class2(self, text):
        """
        TODO:和home一样
        """

    def simple_search(self):
        """
        TODO:和home的一样，区别search条件多了一个显示上架/未上架图书的选项combobox_filter，根据它进行查询
             这里第一列是封面，插入图片的方法看下方例子
        """
        self.tableWidget.insertRow(0)
        # item = QTableWidgetItem('test')  # 封装内容 QTableWidgetItem(这里必须是字符串!)
        # item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
        # item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)  # 禁止修改表内元素+可以勾选
        # item.setCheckState(QtCore.Qt.Unchecked)
        # self.tableWidget.setItem(0,0,item)  # 插入内容 i 为行， 后一个参数为列
        # path = './icon/test_pic.jpg'
        # item = QTableWidgetItem(QtGui.QIcon(QtGui.QPixmap(path).scaled(QtCore.QSize(100, 100), Qt.KeepAspectRatio)),'')
        # item = QTableWidgetItem(QtGui.QIcon(QtGui.QPixmap(path)), '')
        # item = QTableWidgetItem(QtGui.QIcon(path), '格式')
        # item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
        # item.setCheckState(QtCore.Qt.Unchecked)
        # self.tableWidget.setItem(0,0,item)

    def detail_search(self, search_option):
        """
        TODO:同上，注意这里传来的search_option依然是高级查询的选项，还要结合显示信息和排序信息进行搜索
        """

    def refresh_filter(self, text):
        """
        TODO:这个函数在改变显示内容即已上架/未上架/全部时自动调用，先判断当前查询条件时简单查询还是复杂查询，
             然后把新的显示内容选项覆盖当前搜索条件的显示内容项 然后重新调用查询 相当于刷新
        """

    def refresh_sort(self, text):
        """
        TODO: 这个函数在改变排序方式即已上架/未上架/全部时自动调用，和上面的函数一个意思
        """

    def refresh_current_page(self):
        """
        TODO:看下现在是第几页，在当前查询条件下重新跳到这一页刷新一下，在更改书目信息或是新增书目后会自动调用该函数
             有可能出现的情况是在下面下架或删除书的函数里调用该函数，由于一次下架删除很多书导致当前页数不存在
             所以这个函数可以先按当前查询条件用上面的函数查一下若页数存在则跳往此页，若不存在则跳往最后一页
        """

    def last_page(self):
        """
        TODO:同home，但查询条件多了显示内容以及排序
        """

    def next_page(self):
        """
        TODO:同上
        """

    def page_jump(self):
        """
        TODO:同上
        """

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:同home
        """
        self.book_id = 'I come from home'
        self.book_detail()

    def down_book(self):
        """
        TODO:点击下架按钮触发该函数，把勾选的行对应的书状态变为下架
             判断第row行是否被勾选的办法: if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked
             若已被勾选则会通过if判断
             数据库更新完后 self.refresh_current_page刷新一下当前页面
        """

    def up_book(self):
        """
        TODO:上面那个注释里 下改成上
        """

    def delete_book(self):
        """
        TODO:上面那个注释里 上架改成删除 删除前提示一下是否要删除
        """

    def get_image_label(self, image):
        image_label = QtWidgets.QLabel(self.centralwidget)
        image_label.setText('')
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap(image)
        image_label.setPixmap(pixmap)
        return image_label

    def add_book(self):
        self.switch_add_book.emit()

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

    def show_user(self):
        self.switch_user.emit()

    def show_press(self):
        self.switch_press.emit()

    def book_detail(self):
        self.switch_book_detail.emit()

    def detail_search_window(self):
        self.switch_detail_research.emit()

    def show_order(self):
        self.switch_order.emit()