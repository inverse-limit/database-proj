import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_register_window import *
from PyQt5.QtCore import Qt
import pyodbc


class register_window(QDialog, Ui_register_window):
    def __init__(self, parent=None):
        super(register_window, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_accept.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def accept(self):
        '''
        TODO:点击确认按钮后自动调用该函数，需要将用户注册时填入的信息加入数据库
             变量名都和报告视频里数据库设计里的一样，也可在ui_register_window.py中找到
             比如用户账号为 self.u_account.text() 字符串类型 用户密码为 self.u_pswd.text() 字符串类型
             输入数据库前进行验证：用户名和密码是否符合要求
                                 密码和验证密码是否相同
                                 电话是否符合格式
                                 邮箱是否符合格式
                                 邀请码是否在数据库中
                                 可能还有其他的
        '''
        check = self.database.register_function(self.u_account.text(), self.u_pswd.text(), self.u_name.text(),
                                                self.u_telephone.text(), self.u_email.text(), self.invite.text(),
                                                self.check_pswd.text())
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '用户名已存在！')
        if check == 9:
            QtWidgets.QMessageBox.about(self, '提示', '邀请码已被使用！')
        if check == 6:
            QtWidgets.QMessageBox.about(self, '提示', '用户名过长！')
        if check == 5:
            QtWidgets.QMessageBox.about(self, '提示', '两次输入密码不一致！')
        if check == 1:
            QtWidgets.QMessageBox.about(self, '提示', '邀请码不存在！')
        if check == 3:
            QtWidgets.QMessageBox.about(self, '提示', '电话不符合格式！')
        if check == 4:
            QtWidgets.QMessageBox.about(self, '提示', '邮箱不符合格式！')
        if check == 7:
            QtWidgets.QMessageBox.about(self, '提示', '密码过短！')
        if check == 8:
            QtWidgets.QMessageBox.about(self, '提示', '密码过长！')
        if check == 2:
            QtWidgets.QMessageBox.about(self, '提示', '注册成功!')
            self.done(1)  # 退出窗口

    def cancel(self):
        self.done(-1)