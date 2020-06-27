import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui_detail_search import *


class detail_research(QtWidgets.QDialog, Ui_detail_search_window):

    def __init__(self, parent=None):
        super(detail_research, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.close)

        stock_status = ['有货', '缺货']
        self.comboBox_stock.addItems(stock_status)