import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_login_window import *


class login_window(QtWidgets.QMainWindow, Ui_login_window):
    switch_home = QtCore.pyqtSignal()  # 登录跳转到主页信号
    switch_register = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(login_window, self).__init__(parent)
        self.setupUi(self)
        self.user_data = None  # 用于保存用户资料
        self.pushButton_register.clicked.connect(self.register)  # 注册按钮连接打开注册窗口函数
        self.pushButton_log.clicked.connect(self.login)  # 登录进入主页

    def register(self):
        self.switch_register.emit()

    def login(self):
        """
        TODO:调用数据库验证用户账号和密码，没有匹配的则跳出提示用户名或密码错误QMessagebox用法在action_register里有
             匹配的就查询用户信息并用你想要的方式保存到self.user_data，也就是个人信息页上的那些信息，会员状态有：
             非会员，是会员加到期时间
             保存的self.user_data我会传到home界面类到时候一样可调用也即action_home_window里的self.user_data和这里一样
             之后各种地方的函数自动传入的user_data数据都是现在这个格式，在修改个人信息界面处修改了之后也会相应改变
             操作完成后self.switch_home.emit()切换到home界面
        """
        self.user_data = 'I am user_data'
        self.switch_home.emit()
