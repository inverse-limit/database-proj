# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_register_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_window(object):
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(313, 374)
        register_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(register_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.u_account_label = QtWidgets.QLabel(register_window)
        self.u_account_label.setObjectName("u_account_label")
        self.horizontalLayout.addWidget(self.u_account_label)
        self.u_account = QtWidgets.QLineEdit(register_window)
        self.u_account.setText("")
        self.u_account.setObjectName("u_account")
        self.horizontalLayout.addWidget(self.u_account)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.u_pswd_label = QtWidgets.QLabel(register_window)
        self.u_pswd_label.setObjectName("u_pswd_label")
        self.horizontalLayout_2.addWidget(self.u_pswd_label)
        self.u_pswd = QtWidgets.QLineEdit(register_window)
        self.u_pswd.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_pswd.setText("")
        self.u_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.u_pswd.setObjectName("u_pswd")
        self.horizontalLayout_2.addWidget(self.u_pswd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_pswd_label = QtWidgets.QLabel(register_window)
        self.check_pswd_label.setObjectName("check_pswd_label")
        self.horizontalLayout_3.addWidget(self.check_pswd_label)
        self.check_pswd = QtWidgets.QLineEdit(register_window)
        self.check_pswd.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.check_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.check_pswd.setObjectName("check_pswd")
        self.horizontalLayout_3.addWidget(self.check_pswd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.u_name_label = QtWidgets.QLabel(register_window)
        self.u_name_label.setObjectName("u_name_label")
        self.horizontalLayout_4.addWidget(self.u_name_label)
        self.u_name = QtWidgets.QLineEdit(register_window)
        self.u_name.setObjectName("u_name")
        self.horizontalLayout_4.addWidget(self.u_name)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.u_telephone_label = QtWidgets.QLabel(register_window)
        self.u_telephone_label.setObjectName("u_telephone_label")
        self.horizontalLayout_5.addWidget(self.u_telephone_label)
        self.u_telephone = QtWidgets.QLineEdit(register_window)
        self.u_telephone.setObjectName("u_telephone")
        self.horizontalLayout_5.addWidget(self.u_telephone)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.u_email_label = QtWidgets.QLabel(register_window)
        self.u_email_label.setObjectName("u_email_label")
        self.horizontalLayout_6.addWidget(self.u_email_label)
        self.u_email = QtWidgets.QLineEdit(register_window)
        self.u_email.setObjectName("u_email")
        self.horizontalLayout_6.addWidget(self.u_email)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.invite_label = QtWidgets.QLabel(register_window)
        self.invite_label.setObjectName("invite_label")
        self.horizontalLayout_8.addWidget(self.invite_label)
        self.invite = QtWidgets.QLineEdit(register_window)
        self.invite.setText("")
        self.invite.setObjectName("invite")
        self.horizontalLayout_8.addWidget(self.invite)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_accept = QtWidgets.QPushButton(register_window)
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.horizontalLayout_7.addWidget(self.pushButton_accept)
        self.pushButton_cancel = QtWidgets.QPushButton(register_window)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_7.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "注册"))
        self.u_account_label.setText(_translate("register_window", "用户名"))
        self.u_account.setPlaceholderText(_translate("register_window", "不超过10个字节的汉字、字母、数字"))
        self.u_pswd_label.setText(_translate("register_window", "密码"))
        self.u_pswd.setPlaceholderText(_translate("register_window", "8到10位的字母或数字"))
        self.check_pswd_label.setText(_translate("register_window", "重复密码"))
        self.u_name_label.setText(_translate("register_window", "姓名"))
        self.u_telephone_label.setText(_translate("register_window", "电话"))
        self.u_telephone.setPlaceholderText(_translate("register_window", "11位数字"))
        self.u_email_label.setText(_translate("register_window", "邮箱"))
        self.invite_label.setText(_translate("register_window", "邀请码"))
        self.invite.setPlaceholderText(_translate("register_window", "可选，用于平台邀请的客户"))
        self.pushButton_accept.setText(_translate("register_window", "确认"))
        self.pushButton_cancel.setText(_translate("register_window", "取消"))
