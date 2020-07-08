import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_m_user_profile import *
import time


class m_user_profile(QtWidgets.QWidget, Ui_m_user_profile):
    switch_cart = QtCore.pyqtSignal()
    switch_order = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(m_user_profile, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_cart.clicked.connect(self.show_cart)
        self.pushButton_order.clicked.connect(self.show_order)
        self.user_id = 1  # 测试

    def put_in_user_data(self, user_id):
        """
        TODO:类似Home的逻辑，双击用户管理表的一行给进来一个user_id，用它填信息并存到self.user_id里
        """
        row = self.database.m_user_profile(user_id)
        self.user_id = user_id
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if row.vip_status >= date:
            sta = '会员有效期至 ' + str(row.vip_status)
        else:
            sta = '非会员'
        self.u_account.setText(row.u_account)
        self.u_nickname.setText(row.u_nickname)
        self.u_name.setText(row.u_name)
        self.u_telephone.setText(row.u_telephone)
        self.u_email.setText(row.u_email)
        self.vip_status.setText(sta)
        self.u_address1_2.setPlainText(row.u_address1)
        self.u_address2.setText(row.u_address2)

        # self.u_account.setText('张三')  # 设置用户名
        # self.u_nickname.setText('安安')  # 昵称
        # self.u_name.setText('阿斯蒂')  # 真实姓名
        # self.u_telephone.setText('918273')  # 电话号码
        # self.u_email.setText('asdf@adsf.com')  # 邮箱
        # self.vip_status.setText('vip会员至2020年9月3日')  # 会员状态
        # self.u_address1.setPlainText('埃里克就')  # 地址1
        # self.u_address2.setPlainText('阿斯蒂芬')  # 地址2

    def show_cart(self):
        self.switch_cart.emit()

    def show_order(self):
        self.switch_order.emit()
