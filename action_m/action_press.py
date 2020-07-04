import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_press import *


class press(QtWidgets.QWidget, Ui_press):
    switch_detail_press = QtCore.pyqtSignal()
    switch_add = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(press, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_add_press.clicked.connect(self.switch_add_window)

    def search(self):
        """
        TODO:点击查询按钮进行搜索，搜索条件有框里的字和radioButton_press_name和radioButton_person
        """

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的press_id存到self.press_id里，然后切换到出版社详情用这个填信息
        """
        self.press_id = 'I am press_id'
        self.press_detail()

    def switch_add_window(self):
        self.switch_add.emit()

    def press_detail(self):
        self.switch_detail_press.emit()