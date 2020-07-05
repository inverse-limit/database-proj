import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_home_window import *
import math


class home_window(QtWidgets.QMainWindow, Ui_home_window):
    switch_detail_research = QtCore.pyqtSignal()
    switch_user_profile = QtCore.pyqtSignal()
    switch_cart = QtCore.pyqtSignal()
    switch_contactus = QtCore.pyqtSignal()
    switch_book_detail = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(home_window, self).__init__(parent)
        self.setupUi(self)
        # 跳转链接
        self.pushButton_detail_search.clicked.connect(self.detail_search_window)
        self.pushButton_cart.clicked.connect(self.cart_window)
        self.pushButton_u_profile.clicked.connect(self.user_profile_window)
        self.pushButton_contact.clicked.connect(self.contactus_window)
        # 功能按钮
        self.pushButton_search.clicked.connect(self.simple_search)
        self.pushButton_last_page.clicked.connect(self.last_page)
        self.pushButton_next_page.clicked.connect(self.next_page)
        self.pushButton_page_jump.clicked.connect(self.page_jump)
        self.comboBox_class1.activated[str].connect(self.get_class2)
        self.comboBox_class2.addItem('...')
        self.user_data = 1  # 用户信息，这里改没有用处，它是从login和edit_user_profile传过来的
        self.search_option = None  # 查询条件
        self.cart_content = None  # 购物车信息

    def put_in_data(self):
        """
        TODO:给主界面左边的图书分类选项框输入所有大类作为候选项
             添加方法：把类别作为字符串放进一个列表，然后self.combobox_class1.addItems(列表)
             默认也就是列表的第一个应该是'...'表示所有类别，它没有子分类
             当用户切换大类时会自动触发下面的get_class2函数，函数的输入值text就是此时框内的字符，利用它把子类的数据给到小类框
             下面为添加元素的例子
        """
        # sample---------------------------
        listt = self.database.home_class()
        self.comboBox_class1.addItems(listt)
        # sample-----------------------------

    def get_class2(self, text):
        """
        TODO:用户点击表示大类的分类框1触会发该函数把大类框当前选项作为text参数传进来，
             需要基于它把相应小类给到右边的选项框里
             小类的第一个是'...'表示全部分类，用self.combobox.clear()可删除当前选项框里保存的所有内容
             以下代码为基于大类给小类输入元素的例子
        """
        self.comboBox_class2.clear()
        listt = self.database.home_class2(text)
        self.comboBox_class2.addItems(listt)

    def simple_search(self):
        """
        TODO:用户点击主界面上的查询按钮进行查询，触发该函数，有以下检索条件
             分类：self.combobox_classi(i=1,2).currentText() 字符串
             文字框：self.lineEdit_search.text() 字符串
             按书名和按作者的按钮：self.radioButton_name.isChecked() self.radioButton_author.isChecked() bool 型
             建议把这些内容在这函数里先按你想要的方式存放到self.simple_search_option里面，这样下面翻页函数也可直接调用
             否则调用翻页函数时它取当前的查询栏数据进行检索时可能会出现我点了查询按钮后又去动了查询栏结果翻页是按动了之后的结果
             查询的后果
             在数据库中检索后插入到页面，一页插个12行左右
             这个函数只查询第一页的书应该就够了，数据库那里直接查询整个表然后给到电脑内存里不太合理
             下面的代码作为例子打印了上面的变量并且把搜索框里的字插入到表格书名列里插了五行
             搜索能够模糊匹配
             把总页数和当前页数标签更新一下:
             self.label_all_page.setText(共 n 页) self.label_all_page.setText(第 1 页) 注意空格，没有结果总页数也是1页
        """
        self.tableWidget.setRowCount(0)
        self.search_option = [self.comboBox_class1.currentText(), self.comboBox_class2.currentText(),
                                self.lineEdit_search.text(), self.radioButton_name.isChecked(),
                                self.radioButton_author.isChecked()]
        # print(self.comboBox_class1.currentText())
        # print(self.lineEdit_search.text())
        # print(self.radioButton_name.isChecked())
        #
        self.row = self.database.home_simple_search(self.search_option)
        n = len(self.row)
        self.page_now = 1
        for i in range(0, min(n, 1*12)):
            self.tableWidget.insertRow(i)  # 插入一行
            item0 = QTableWidgetItem(self.row[i].book_id)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item0)
            item1 = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item1.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item1.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item1)
            item2 = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item2.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item2.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item2)
            item3 = QTableWidgetItem(self.row[i].c)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item3.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item3.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item3)
            item4 = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item4.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item4.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item4)
            item5 = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item5.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item5.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 5, item5)
            item6 = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item6.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item6.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 6, item6)
            item7 = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item7.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item7.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 7, item7)
        self.label_all_page.setText("共" + str(math.ceil(n/12)) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")

    def detail_search(self, search_option):
        """
        TODO:高级查询窗口的确认按钮点击后会自动把detail_search类的self.search_option(见action_detail_search.py的accept函数)
             传入这个函数并调用，利用它进行检索并同上把查询到的数据插入画面
             同样因为要翻页建议先把search_option存到self.detail_search_option里给翻页函数用
        """
        self.tableWidget.setRowCount(0)
        self.search_option = search_option
        self.row = self.database.detail_search_result(search_option)
        n = len(self.row)
        self.page_now = 1
        for i in range(0, min(n, 1 * 12)):
            self.tableWidget.insertRow(i)  # 插入一行
            item0 = QTableWidgetItem(self.row[i].book_id)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 0, item0)
            item1 = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item1.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item1.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 1, item1)
            item2 = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item2.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item2.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 2, item2)
            item3 = QTableWidgetItem(self.row[i].c)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item3.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item3.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 3, item3)
            item4 = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item4.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item4.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 4, item4)
            item5 = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item5.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item5.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 5, item5)
            item6 = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item6.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item6.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 6, item6)
            item7 = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item7.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item7.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i, 7, item7)
        self.label_all_page.setText("共" + str(math.ceil(n/12)) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")

    def last_page(self):
        """
        TODO:点击上一页时触发该函数，查询相应内容填到表格里，并且把当前页码更新一下
        """
        self.tableWidget.setRowCount(0)  # 使用这行代码清空当前表格
        n = len(self.row)
        self.page_now -= 1
        for i in range((self.page_now-1)*12, min(n, self.page_now * 12)):
            self.tableWidget.insertRow(i - (self.page_now-1)*12)  # 插入一行
            item0 = QTableWidgetItem(self.row[i].book_id)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 0, item0)
            item1 = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item1.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item1.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 1, item1)
            item2 = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item2.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item2.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 2, item2)
            item3 = QTableWidgetItem(self.row[i].c)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item3.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item3.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 3, item3)
            item4 = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item4.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item4.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 4, item4)
            item5 = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item5.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item5.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 5, item5)
            item6 = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item6.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item6.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 6, item6)
            item7 = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item7.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item7.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now-1)*12, 7, item7)
        self.label_all_page.setText("共" + str(math.ceil(n/12)) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")


    def next_page(self):
        """
        TODO:下一页
        """
        self.tableWidget.setRowCount(0)  # 使用这行代码清空当前表格
        n = len(self.row)
        self.page_now += 1
        for i in range((self.page_now - 1) * 12, min(n, self.page_now * 12)):
            self.tableWidget.insertRow(i - (self.page_now - 1) * 12)  # 插入一行
            item0 = QTableWidgetItem(self.row[i].book_id)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 0, item0)
            item1 = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item1.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item1.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 1, item1)
            item2 = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item2.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item2.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 2, item2)
            item3 = QTableWidgetItem(self.row[i].c)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item3.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item3.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 3, item3)
            item4 = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item4.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item4.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 4, item4)
            item5 = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item5.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item5.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 5, item5)
            item6 = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item6.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item6.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 6, item6)
            item7 = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
            item7.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            item7.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
            self.tableWidget.setItem(i - (self.page_now - 1) * 12, 7, item7)
        self.label_all_page.setText("共" + str(math.ceil(n/12)) + "页")
        self.label_current_page.setText("第" + str(self.page_now) + "页")

    def page_jump(self):
        """
        TODO:跳转到指定页
             跳转输入框内容：self.lineEdit_pagejump.text()
             对输入内容做下检测 应该是正整数
        """
        n = len(self.row)
        if isinstance(self.lineEdit_pagejump,int):
            if self.lineEdit_pagejump > 0 and self.lineEdit_pagejump <= math.ceil(n/12):
                self.tableWidget.setRowCount(0)  # 使用这行代码清空当前表格
                self.page_now = self.lineEdit_pagejump
                for i in range((self.page_now - 1) * 12, min(n, self.page_now * 12)):
                    self.tableWidget.insertRow(i - (self.page_now - 1) * 12)  # 插入一行
                    item0 = QTableWidgetItem(self.row[i].book_id)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item0.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 0, item0)
                    item1 = QTableWidgetItem(self.row[i].book_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item1.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item1.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 1, item1)
                    item2 = QTableWidgetItem(self.row[i].author_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item2.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item2.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 2, item2)
                    item3 = QTableWidgetItem(self.row[i].c)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item3.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item3.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 3, item3)
                    item4 = QTableWidgetItem(self.row[i].press_name)  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item4.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item4.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 4, item4)
                    item5 = QTableWidgetItem(str(self.row[i].s_price))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item5.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item5.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 5, item5)
                    item6 = QTableWidgetItem(str(self.row[i].mon_sell))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item6.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item6.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 6, item6)
                    item7 = QTableWidgetItem(str(self.row[i].reserve))  # 封装内容 QTableWidgetItem(这里必须是字符串!)
                    item7.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
                    item7.setFlags(QtCore.Qt.ItemIsEnabled)  # 禁止修改表内元素
                    self.tableWidget.setItem(i - (self.page_now - 1) * 12, 7, item7)
                self.label_all_page.setText("共" + str(math.ceil(n/12)) + "页")
                self.label_current_page.setText("第" + str(self.page_now) + "页")
        else:
            QtWidgets.QMessageBox.about(self, '提示', '输入的不是正整数或超过了总页数！')

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:用户双击表格后自动调用该函数，row, column为双击位置的行列数
             利用这个把你想要的东西存到self.book_id里，我会把self.book_id
             传送到book_detail类 在图书详情页面你需要利用那边的self.book_id调出图书信息填到界面里
        """
        n = (self.page_now - 1) * 12 + row
        infor = self.row[n]
        self.book_id = infor.book_id
        self.switch_book_detail.emit()

    # 跳转
    def detail_search_window(self):
        self.switch_detail_research.emit()

    def user_profile_window(self):
        self.switch_user_profile.emit()

    def cart_window(self):
        self.switch_cart.emit()

    def book_detail(self):
        self.switch_book_detail.emit()

    def contactus_window(self):
        self.switch_contactus.emit()
