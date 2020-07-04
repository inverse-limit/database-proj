import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_user_manage import *


class user_manage(QtWidgets.QWidget, Ui_user_manage):
    switch_user_profile = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(user_manage, self).__init__(parent)
        self.setupUi(self)
        self.comboBox_vip_status.addItems(['非会员','会员','作家用户'])
        self.pushButton_search.clicked.connect(self.search)

    def search(self):
        """
        TODO:点击查询按钮根据lineEdit_search radioButton_account radioButton_nickname
             dateEdit_date1 dateEdit_date2 combobox_vip_status
        """
        self.tableWidget.insertRow(0)

    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        TODO:和home类似把相应行的user_id存到self.press_id里，然后切换到用户详情用这个填信息
        """
        self.user_id = 'I am press_id'
        self.user_detail()

    def user_detail(self):
        self.switch_user_profile.emit()