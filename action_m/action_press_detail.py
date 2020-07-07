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
            self.press_id = press_id
            row = self.database.m_press_detail(press_id)
            self.press_name.setText(row.press_name)
            self.person.setText(row.person)
            self.telephone.setText(str(row.telephone))
            self.email.setText(row.email)
            self.address.setPlainText(row.address)

    def save(self):
        """
        TODO:如果self.press_id不为None, 说明是双击表格进来的，把对图书馆详细信息的改动保存到数据库
             如果self.press_id为None,说明是新增书目进来的，检验下界面里的格子是不是都填了
             然后把新出版社的信息放到数据库
        """

        option = [self.press_name.text(), self.person.text(), self.telephone.text(),
                  self.email.text(), self.address.toPlainText()]
        check = self.database.m_press_save(self.press_id, option)
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '社名为空！')
        if check == 1:
            QtWidgets.QMessageBox.about(self, '提示', '联系人为空！')
        if check == 2:
            QtWidgets.QMessageBox.about(self, '提示', '联系电话为空！')
        if check == 3:
            QtWidgets.QMessageBox.about(self, '提示', '电子邮箱为空！')
        if check == 4:
            QtWidgets.QMessageBox.about(self, '提示', '地址为空！')
        if check == 5:
            QtWidgets.QMessageBox.about(self, '提示', '保存成功！')
        self.switch_save.emit()
