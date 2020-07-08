import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_manage import *
import math


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
        self.tableWidget.setColumnWidth(0,4)
        self.tableWidget.setColumnWidth(1,90)
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
        self.search_option = None
        self.page_now = 1

    def put_in_data(self):
        """
        TODO:和home一样
        """
        listt = self.database.home_class()
        self.comboBox_class1.addItems(listt)

    def get_class2(self, text):
        """
        TODO:和home一样
        """
        self.comboBox_class2.clear()
        listt = self.database.home_class2(text)
        self.comboBox_class2.addItems(listt)

    def simple_search(self):
        """
        TODO:和home的一样，区别search条件多了一个显示上架/未上架图书的选项combobox_filter，以及排序的combobox_sort,
             根据它进行查询, 插入图片的方法看下方例子
        """
        self.tableWidget.setRowCount(0)
        self.search_option = [self.comboBox_class1.currentText(), self.comboBox_class2.currentText(),
                              self.lineEdit_search.text(), self.radioButton_name.isChecked(),
                              self.radioButton_author.isChecked()]
        self.row = self.database.manage_simple_search(self.search_option, self.comboBox_filter.currentText(),
                                                      self.comboBox_sort.currentText())
        n = len(self.row)
        self.page_now = 1
        for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
            self.tableWidget.insertRow(i)
            # 第一列固定这么加
            item = QtWidgets.QTableWidgetItem('')
            item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(i,0,item)

            # 第二列封面
            if self.row[i].graph:
                path = self.row[i].graph
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 1, item)
            else:
                path = './icon/no_cover.jpg'
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 1, item)

            item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item)

            item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item)

            item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item)

            item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 5, item)

            item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 6, item)

            item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 7, item)

            item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 8, item)

            if self.row[i].on_sale == 'on':
                sta = '已上架'
            else:
                sta = '未上架'
            item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 9, item)
        self.page_all = math.ceil(n/6)
        self.label_all_page.setText("共" + str(self.page_all) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")

    def detail_search(self, search_option):
        """
        TODO:同上，注意这里传来的search_option依然是高级查询的选项，还要结合显示信息和排序信息进行搜索
        """
        self.tableWidget.setRowCount(0)
        self.search_option = search_option
        self.row = self.database.manage_detail_search(self.search_option, self.comboBox_filter.currentText(),
                                                      self.comboBox_sort.currentText())
        n = len(self.row)
        self.page_now = 1
        for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
            self.tableWidget.insertRow(i)
            # 第一列固定这么加
            item = QtWidgets.QTableWidgetItem('')
            item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(i, 0, item)

            # 第二列封面
            if self.row[i].graph:
                path = self.row[i].graph
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 1, item)
            else:
                path = './icon/no_cover.jpg'
                item = self.get_image_label(path)
                self.tableWidget.setCellWidget(i, 1, item)

            item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item)

            item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item)

            item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item)

            item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 5, item)

            item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 6, item)

            item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 7, item)

            item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 8, item)

            if self.row[i].on_sale == 'on':
                sta = '已上架'
            else:
                sta = '未上架'
            item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 9, item)
        self.page_all = math.ceil(n/6)
        self.label_all_page.setText("共" + str(self.page_all) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")

    def refresh_filter(self, text):
        """
        TODO:这个函数在改变显示内容即已上架/未上架/全部 时自动调用，先判断当前查询条件时简单查询还是复杂查询，
             然后把新的 显示内容 选项覆盖当前搜索条件的显示内容项 然后重新调用查询 相当于刷新
        """
        if self.search_option:
            if len(self.search_option) == 5:
                self.simple_search()
            else:
                self.detail_search(self.search_option)
        else:
            pass

    def refresh_sort(self, text):
        """
        TODO: 这个函数在改变排序方式即已上架/未上架/全部 时自动调用，先判断当前查询条件时简单查询还是复杂查询，
              然后把新的 排序 选项覆盖当前搜索条件的 排序 项 然后重新调用查询 相当于刷新
        """
        if self.search_option:
            if len(self.search_option) == 5:
                self.simple_search()
            else:
                self.detail_search(self.search_option)
        else:
            pass

    def refresh_current_page(self):
        """
        TODO:看下现在是第几页，在当前查询条件下重新跳到这一页刷新一下，在更改书目信息或是新增书目后会自动调用该函数
             有可能出现的情况是在下面下架或删除书的函数里调用该函数，由于一次下架删除很多书导致当前页数不存在
             所以这个函数可以先按当前查询条件用上面的函数查一下若页数存在则跳往此页，若不存在则跳往最后一页
        """
#        m = self.page_now
        if self.search_option is None:
            pass
        else:
            if len(self.search_option) == 5:
                self.simple_search()
            else:
                self.detail_search(self.search_option)
            # if m <= self.page_all:
            #     self.tableWidget.setRowCount(0)
            #     n = len(self.row)
            #     self.page_now = m
            #     print(n)
            #     print(self.page_now)
            #     for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
            #         self.tableWidget.insertRow(i)
            #         # 第一列固定这么加
            #         item = QtWidgets.QTableWidgetItem('')
            #         item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            #         item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            #         item.setCheckState(QtCore.Qt.Unchecked)
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 0, item)
            #
            #         # 第二列封面
            #         if self.row[i].graph:
            #             path = self.row[i].graph
            #             item = self.get_image_label(path)
            #             self.tableWidget.setCellWidget(i, 1, item)
            #         else:
            #             path = './icon/no_cover.jpg'
            #             item = self.get_image_label(path)
            #             self.tableWidget.setCellWidget(i, 1, item)
            #
            #         item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 2, item)
            #
            #         item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 3, item)
            #
            #         item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 4, item)
            #
            #         item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 5, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 6, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 7, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 8, item)
            #
            #         if self.row[i].on_sale == 'on':
            #             sta = '已上架'
            #         else:
            #             sta = '未上架'
            #         item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 9, item)
            #     self.page_all = math.ceil(n/6)
            #     self.label_all_page.setText("共" + str(self.page_all) + "页")
            #     self.label_current_page.setText("第" + str(self.page_now) + "页")
            # else:
            #     self.tableWidget.setRowCount(0)
            #     n = len(self.row)
            #     self.page_now = self.page_all
            #     for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
            #         self.tableWidget.insertRow(i)
            #         # 第一列固定这么加
            #         item = QtWidgets.QTableWidgetItem('')
            #         item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            #         item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            #         item.setCheckState(QtCore.Qt.Unchecked)
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 0, item)
            #
            #         # 第二列封面
            #         if self.row[i].graph:
            #             path = self.row[i].graph
            #             item = self.get_image_label(path)
            #             self.tableWidget.setCellWidget(i, 1, item)
            #         else:
            #             path = './icon/no_cover.jpg'
            #             item = self.get_image_label(path)
            #             self.tableWidget.setCellWidget(i, 1, item)
            #
            #         item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 2, item)
            #
            #         item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 3, item)
            #
            #         item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 4, item)
            #
            #         item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 5, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 6, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 7, item)
            #
            #         item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 8, item)
            #
            #         if self.row[i].on_sale == 'on':
            #             sta = '已上架'
            #         else:
            #             sta = '未上架'
            #         item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            #         item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            #         item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            #         self.tableWidget.setItem(i - (self.page_now - 1) * 6, 9, item)
            #     self.page_all = math.ceil(n / 6)
            #     self.label_all_page.setText("共" + str(self.page_all) + "页")
            #     self.label_current_page.setText("第" + str(self.page_now) + "页")



    def last_page(self):
        """
        TODO:同home，但查询条件多了显示内容以及排序
        """
        n = len(self.row)
        self.page_now -= 1
        if self.page_now == 0:
            self.page_now = 1
            pass
        else:
            self.tableWidget.setRowCount(0)
            for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
                self.tableWidget.insertRow(i - (self.page_now - 1) * 6)
                # 第一列固定这么加
                item = QtWidgets.QTableWidgetItem('')
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 0, item)

                # 第二列封面
                if self.row[i].graph:
                    path = self.row[i].graph
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)
                else:
                    path = './icon/no_cover.jpg'
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)

                item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 2, item)

                item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 3, item)

                item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 4, item)

                item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 5, item)

                item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 6, item)

                item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 7, item)

                item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 8, item)

                if self.row[i].on_sale == 'on':
                    sta = '已上架'
                else:
                    sta = '未上架'
                item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 9, item)
            self.page_all = math.ceil(n / 6)
            self.label_all_page.setText("共" + str(self.page_all) + "页")
            self.label_current_page.setText("第" + str(self.page_now) + "页")

    def next_page(self):
        """
        TODO:同上
        """
        n = len(self.row)
        self.page_now += 1
        if self.page_now > self.page_all:
            self.page_now = self.page_all
            pass
        else:
            self.tableWidget.setRowCount(0)
            for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
                self.tableWidget.insertRow(i - (self.page_now - 1) * 6)
                # 第一列固定这么加
                item = QtWidgets.QTableWidgetItem('')
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 0, item)

                # 第二列封面
                if self.row[i].graph:
                    path = self.row[i].graph
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)
                else:
                    path = './icon/no_cover.jpg'
                    item = self.get_image_label(path)
                    self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)

                item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 2, item)

                item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 3, item)

                item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 4, item)

                item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 5, item)

                item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 6, item)

                item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 7, item)

                item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 8, item)

                if self.row[i].on_sale == 'on':
                    sta = '已上架'
                else:
                    sta = '未上架'
                item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                self.tableWidget.setItem(i - (self.page_now - 1) * 6, 9, item)
            self.page_all = math.ceil(n / 6)
            self.label_all_page.setText("共" + str(self.page_all) + "页")
            self.label_current_page.setText("第" + str(self.page_now) + "页")

    def page_jump(self):
        """
        TODO:同上
        """
        if self.row:
            self.tableWidget.setRowCount(0)
            n = len(self.row)
            if self.lineEdit_pagejump.text().isdigit():
                if int(self.lineEdit_pagejump.text()) >0 and int(self.lineEdit_pagejump.text()) <= math.ceil(n/6):
                    self.tableWidget.setRowCount(0)
                    self.page_now = int(self.lineEdit_pagejump.text())
                    for i in range((self.page_now - 1) * 6, min(n, self.page_now * 6)):
                        self.tableWidget.insertRow(i - (self.page_now - 1) * 6)
                        # 第一列固定这么加
                        item = QtWidgets.QTableWidgetItem('')
                        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 0, item)

                        # 第二列封面
                        if self.row[i].graph:
                            path = self.row[i].graph
                            item = self.get_image_label(path)
                            self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)
                        else:
                            path = './icon/no_cover.jpg'
                            item = self.get_image_label(path)
                            self.tableWidget.setCellWidget(i - (self.page_now - 1) * 6, 1, item)

                        item = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 2, item)

                        item = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 3, item)

                        item = QTableWidgetItem(self.row[i].cl)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 4, item)

                        item = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 5, item)

                        item = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 6, item)

                        item = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 7, item)

                        item = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 8, item)

                        if self.row[i].on_sale == 'on':
                            sta = '已上架'
                        else:
                            sta = '未上架'
                        item = QTableWidgetItem(sta)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                        self.tableWidget.setItem(i - (self.page_now - 1) * 6, 9, item)
                    self.page_all = math.ceil(n / 6)
                    self.label_all_page.setText("共" + str(self.page_all) + "页")
                    self.label_current_page.setText("第" + str(self.page_now) + "页")
            else:
                QtWidgets.QMessageBox.about(self, '提示', '输入的不是正整数或超过了总页数！')
        else:
            pass


    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:同home
        """
        n = (self.page_now - 1) *6 + row
        infor = self.row[n]
        self.book_id = infor.book_id
        self.book_detail()

    def down_book(self):
        """
        TODO:点击下架按钮触发该函数，把勾选的行对应的书状态变为下架
             判断第row行是否被勾选的办法: if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked
             若已被勾选则会通过if判断
             数据库更新完后 self.refresh_current_page刷新一下当前页面
        """
        listt = []
        for row in range(0, self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
                n = (self.page_now - 1) * 6 + row
                infor  = self.row[n]
                listt.append(infor.book_id)
        self.database.manage_on_off_de_book(listt, 'down')
        self.refresh_current_page()

    def up_book(self):
        """
        TODO:上面那个注释里 下改成上
        """
        listt = []
        for row in range(0, self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
                n = (self.page_now - 1) * 6 + row
                infor = self.row[n]
                listt.append(infor.book_id)
        self.database.manage_on_off_de_book(listt, 'up')
        self.refresh_current_page()

    def delete_book(self):
        """
        TODO:上面那个注释里 上架改成删除 删除前提示一下是否要删除
        """
        reply = QtWidgets.QMessageBox.question(self, '删除选中项', '确认要删除吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            listt = []
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
                    n = (self.page_now - 1) * 6 + row
                    infor = self.row[n]
                    listt.append(infor.book_id)
            self.database.manage_on_off_de_book(listt, 'delete')
            self.refresh_current_page()

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

    def get_image_label(self, image):
        image_label = QtWidgets.QLabel(self.centralwidget)
        image_label.setText('')
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap(image)
        pixmap.scaled(50, 40, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        return image_label

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