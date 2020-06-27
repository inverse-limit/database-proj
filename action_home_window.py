import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui_home_window import *


class home_window(QtWidgets.QMainWindow, Ui_home_window):
    switch_detail_research = QtCore.pyqtSignal()
    switch_user_profile = QtCore.pyqtSignal()
    switch_cart = QtCore.pyqtSignal()
    switch_contactus = QtCore.pyqtSignal()

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

        """
        TODO:初始化时给主界面左边的图书分类选项框输入所有大类
        添加方法：把类别作为字符串放进一个列表，然后self.combobox_class1.addItems(列表)
        默认也就是列表的第一个应该是'...'表示所有类别，它没有子分类
        当用户切换大类时会自动触发下面的get_class2函数，函数的输入值text就是此时框内的字符，利用它把子类的数据给到小类框
        下面为添加元素的例子
        """
        # sample---------------------------
        listt = ['...', '211111', '311111']
        self.comboBox_class1.addItems(listt)
        # sample-----------------------------


    def get_class2(self, text):
        """
        TODO:用户点击表示大类的分类框1触发该函数，子类的第一个是'...'表示全部分类，用self.combobox.clear()删除当前所有内容
             以下代码为基于大类给小类输入元素的例子
        """
        self.comboBox_class2.clear()
        print(self.comboBox_class1.currentText())
        if text == '1':
            self.comboBox_class2.addItem('a')
        else:
            self.comboBox_class2.addItem('b')

    def simple_search(self):
        """
        TODO:用户点击主界面上的查询按钮进行查询，触发该函数，有以下检索条件
             分类：self.combobox_classi(i=1,2).currentText() 字符串
             文字框：self.lineEdit_search.text() 字符串
             按书名和按作者的按钮：self.radioButton_name.isChecked() self.radioButton_author.isChecked() bool 型
             在数据库中检索后插入到页面，一页插个12行左右
             下面的代码作为例子打印了上面的变量并且把搜索框里的字插入到表格里插了五行
             搜索能够模糊匹配
        """
        print(self.comboBox_class1.currentText())
        print(self.lineEdit_search.text())
        print(self.radioButton_name.isChecked())

        for i in range(5):
            self.tableWidget.insertRow(i)  # 插入一行
            isbn_item = QTableWidgetItem(self.lineEdit_search.text())  # 封装内容
            isbn_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 格内居中对齐
            # 其他列也一样
            self.tableWidget.setItem(i,0,isbn_item)  # 插入内容 i 为行， 后一个参数为列

    def last_page(self):
        """
        TODO:点击下一页时触发该函数，查询相应内容填到表格里
        """
        self.tableWidget.setRowCount(0)  # 使用这行代码清空当前表格
        pass

    def next_page(self):
        """
        TODO:上一页
        """
        pass

    def page_jump(self):
        """
        TODO:跳转到指定页
             跳转输入框内容：self.lineEdit_pagejump.text()
             对输入内容做下检测 应该是正整数
        """
        pass

    # 跳转
    def detail_search_window(self):
        self.switch_detail_research.emit()

    def user_profile_window(self):
        self.switch_user_profile.emit()

    def cart_window(self):
        self.switch_cart.emit()

    def contactus_window(self):
        self.switch_contactus.emit()
