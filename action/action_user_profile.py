import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_user_profile import *
from ui.ui_edit_user_profile import *
from ui.ui_buy_vip import *


class user_profile(QtWidgets.QWidget, Ui_user_profile):
    switch_edit_profile = QtCore.pyqtSignal()
    switch_buy_vip = QtCore.pyqtSignal()
    switch_login = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(user_profile, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_edit_profile.clicked.connect(self.edit_user_profile)
        self.pushButton_buy_membership.clicked.connect(self.buy_vip)
        self.pushButton_logout.clicked.connect(self.logout)

    def put_in_user_data(self, user_data):
        """
        TODO:user_data就是登录的时候保存的self.user_data会自动当作参数user_data传进来
             包含用户名、昵称、真实姓名、电话、邮箱、会员状态、收货地址1、收获地址2
             如果某一项没有就是'未设置'
             将user_data里的这些内容填到窗口里，下面为示例
        """
        self.u_account.setText(user_data[0])
        self.u_nickname.setText(user_data[1])
        self.u_name.setText(user_data[2])
        self.u_telephone.setText(user_data[3])
        self.u_email.setText(user_data[4])
        self.vip_status.setText(user_data[5])
        self.u_address1.setText(user_data[6])
        self.u_address2.setText(user_data[7])
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

    def buy_vip(self):
        self.switch_buy_vip.emit()

    def logout(self):
        reply = QtWidgets.QMessageBox.question(self, '退出登录', '确认要退出登录吗',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.switch_login.emit()


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
        self.u_account.setText(user_data[0])
        self.u_nickname.setText(user_data[1])
        self.u_name.setText(user_data[2])
        self.u_telephone.setText(user_data[3])
        self.u_email.setText(user_data[4])
        self.u_address1.setPlainText(user_data[6])
        self.u_address2.setPlainText(user_data[7])
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
        check = self.database.user_accept(self.u_account.text(), self.u_nickname.text(), self.u_name.text(),
                                          self.u_telephone.text(), self.u_email.text(), self.u_address1.toPlainText(),
                                          self.u_address2.toPlainText())
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '电话不符合格式！')
        if check == 1:
            QtWidgets.QMessageBox.about(self, '提示', '邮箱不符合格式！')
        if check == 2:
            self.user_data[1] = self.u_nickname.text()
            self.user_data[2] = self.u_name.text()
            self.user_data[3] = self.u_telephone.text()
            self.user_data[4] = self.u_email.text()
            self.user_data[6] = self.u_address1.toPlainText()
            self.user_data[7] = self.u_address2.toPlainText()
            QtWidgets.QMessageBox.about(self, '提示', '修改成功！')
            self.switch_user_profile_accept.emit()  # 这行代码放在最下面不要改

    def cancel(self):
        self.switch_user_profile_cancel.emit()

class buy_vip(QtWidgets.QDialog, Ui_buy_vip):
    switch_user_profile = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(buy_vip, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_accept.clicked.connect(self.accept)

    def accept(self):
        """
        TODO:判断选了哪个radioButton，使数据库里相应用户开通会员或是延长会员时间
        """
        option = [self.radioButton_1.isChecked(), self.radioButton_5.isChecked(), self.radioButton_6.isChecked(),
                  self.radioButton_12.isChecked()]
        account = self.user_data[0]
        check = self.database.buy_vip(account, option)
        if check == 1:
            QtWidgets.QMessageBox.about(self, '提示', '开通成功！')
            self.switch_user_profile.emit()
            self.done(1)
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '请选择开通时间！')

    def cancel(self):
        self.done(-1)

