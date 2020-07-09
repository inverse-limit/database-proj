import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_detail_search import *


class detail_research(QtWidgets.QDialog, Ui_detail_search_window):
    switch_home = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(detail_research, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_accept.clicked.connect(self.accept)
        self.comboBox_class1.activated[str].connect(self.get_class2)
        self.comboBox_class2.addItem('...')
        stock_status = ['有货', '缺货']
        self.comboBox_stock.addItems(stock_status)

    def put_in_data(self):
        """
        TODO:给主界面左边的图书分类选项框输入所有大类作为候选项
             添加方法：把类别作为字符串放进一个列表，然后self.combobox_class1.addItems(列表)
             默认也就是列表的第一个应该是'...'表示所有类别，它没有子分类
             当用户切换大类时会自动触发下面的get_class2函数，函数的输入值text就是此时框内的字符，利用它把子类的数据给到小类框
             下面为添加元素的例子
        """
        listt = self.database.home_class()
        self.comboBox_class1.addItems(listt)

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

    def accept(self):
        """
        TODO:将高级搜索里边所有填了东西的内容以你喜欢的方式保存到self.search_option里面
             啥都不填就警告
        """
        if self.spinBox_price1.value() > self.spinBox_price2.value():
            QtWidgets.QMessageBox.about(self, '提示', '价格下限大于价格上限！')
        else:
            self.search_option = self.database.detail_search(self.lineEdit_ISBN.text(), self.lineEdit_book_name.text(),
                                                             self.lineEdit_author.text(), self.lineEdit_translator.text(),
                                                             self.comboBox_class1.currentText(), self.comboBox_class2.currentText(),
                                                             self.spinBox_price1.value(), self.spinBox_price2.value(),
                                                             self.comboBox_stock.currentText())
            if self.search_option:
                self.switch_home.emit()
            else:
                QtWidgets.QMessageBox.about(self, '提示', '未指定搜索条件！')