import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_press_detail import *


class press_detail(QtWidgets.QWidget, Ui_press_detail):
    switch_save = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(press_detail, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

    def put_in_data(self, press_id=None):
        if press_id:
        # TODO:利用press_id调出出版社信息，
        #      填到界面里，并且存到self.press_id里
            pass

    def save(self):
        """
        TODO:如果self.press_id不为None, 说明是双击表格进来的，把对图书馆详细信息的改动保存到数据库
             如果self.press_id为None,说明是新增书目进来的，检验下界面里的格子是不是都填了
             然后把新出版社的信息放到数据库
        """
        self.switch_save.emit()