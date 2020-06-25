import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui_login_window import *


class login_window(QtWidgets.QMainWindow, Ui_login_window):
    # switch_home = QtCore.pyqtSignal()  # 登录跳转到主页信号
    switch_register = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(login_window, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_register.clicked.connect(self.register)  # 注册按钮连接打开注册窗口函数

    def register(self):
        self.switch_register.emit()
