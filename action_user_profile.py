import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui_user_profile import *
from ui_edit_user_profile import *


class user_profile(QtWidgets.QWidget, Ui_user_profile):
    switch_edit_profile = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(user_profile, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_edit_profile.clicked.connect(self.edit_user_profile)

    def put_in_user_data(self, user_data):
        """
        TODO:user_data就是登录的时候保存的self.user_data会自动当作参数user_data传进来
             包含用户名、昵称、真实姓名、电话、邮箱、会员状态、收货地址1、收获地址2
             如果某一项没有就是'未设置'
             将user_data里的这些内容填到窗口里，下面为示例
        """
        self.u_nickname.setText(user_data)
        # self.u_account.setText('张三')  # 设置用户名
        # self.u_nickname.setText('安安')  # 昵称
        # self.u_name.setText('阿斯蒂')  # 真实姓名
        # self.u_telephone.setText('918273')  # 电话号码
        # self.u_email.setText('asdf@adsf.com')  # 邮箱
        # self.vip_status.setText('vip会员至2020年9月3日')  # 会员状态
        # self.u_address1.setPlainText('埃里克就')  # 地址1
        # self.u_address2.setPlainText('阿斯蒂芬')  # 地址2

    def edit_user_profile(self):
        self.switch_edit_profile.emit()


class edit_user_profile(QtWidgets.QWidget, Ui_edit_user_profile):
    switch_user_profile_accept = QtCore.pyqtSignal()
    switch_user_profile_cancel = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(edit_user_profile, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_accept.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def put_in_user_data(self, user_data):
        """
        TODO:和user_profile类的put_in_data一样把用户数据user_data填到跳出的编辑栏里
             使得用户打开编辑界面框里默认填了当前的信息
        """
        self.user_data = user_data  # 这行代码不要改，保存当前用户信息，下面accept函数需要修改它
        # self.u_account.setText('张三')  # 设置用户名
        # self.u_nickname.setText('安安')  # 昵称
        # self.u_name.setText('阿斯蒂')  # 真实姓名
        # self.u_telephone.setText('918273')  # 电话号码
        # self.u_email.setText('asdf@adsf.com')  # 邮箱
        # self.u_address1.setPlainText('埃里克')  # 地址1
        # self.u_address2.setPlainText('阿斯蒂芬')  # 地址2

    def accept(self):
        """
        TODO:用户在编辑用户个人信息界面点击保存按钮自动调用这个函数
             先检验用户填的信息 若通过将其修改进数据库 并将修改部分更新到上面函数保存的self.user_data里
             务必确保不要改变self.user_data的格式
             然后提示修改成功，执行self.switch_user_profile_accept.emit()语句
             检验不通过比如姓名，地址这些包含特殊字符则提示，不要执行self.switch_user_profile_accept.emit()
        """
        # print(self.u_account.text())  # 取得用户名
        # print(self.u_nickname.text())  # 取得修改的昵称
        # print(self.u_name.text())  # ...
        # print(self.u_telephone.text())
        # print(self.u_email.text())
        # print(self.u_address1.toPlainText())
        # modify self.user_data according to above data
        self.switch_user_profile_accept.emit()  # 这行代码放在最下面不要改

    def cancel(self):
        self.switch_user_profile_cancel.emit()

