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

        stock_status = ['有货', '缺货']
        self.comboBox_stock.addItems(stock_status)

    def accept(self):
        """
        TODO:将高级搜索里边所有填了东西的内容以你喜欢的方式保存到self.search_option里面
             啥都不填就警告
        """
        self.search_option = self.database.detail_search(self.lineEdit_ISBN.text(), self.lineEdit_book_name.text(),
                                                         self.lineEdit_author.text(), self.lineEdit_translator.text(),
                                                         self.comboBox_class1.currentText(), self.comboBox_class2.currentText(),
                                                         self.spinBox_price1.value(), self.spinBox_price2.value(),
                                                         self.comboBox_stock.currentText())
        if self.search_option:
            self.switch_home.emit()
        else:
            QtWidgets.QMessageBox.about(self, '提示', '未指定搜索条件！')