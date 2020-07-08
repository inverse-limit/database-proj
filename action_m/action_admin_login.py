import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_admin_login import *
import pyodbc


class admin_login(QtWidgets.QMainWindow, Ui_admin_login):
    switch_manage = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(admin_login, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_log.clicked.connect(self.login)  # 登录进入主页


    def login(self):
        """
        TODO:检测管理员账号
        """
        check = self.database.login_check(self.u_account.text(), self.u_pswd.text())
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '用户名或密码错误')
        else:
            self.switch_manage.emit()
