# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user_profile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_profile(object):
    def setupUi(self, user_profile):
        user_profile.setObjectName("user_profile")
        user_profile.resize(519, 429)
        self.gridLayout = QtWidgets.QGridLayout(user_profile)
        self.gridLayout.setContentsMargins(20, 20, -1, -1)
        self.gridLayout.setVerticalSpacing(33)
        self.gridLayout.setObjectName("gridLayout")
        self.label_u_account = QtWidgets.QLabel(user_profile)
        self.label_u_account.setObjectName("label_u_account")
        self.gridLayout.addWidget(self.label_u_account, 0, 0, 1, 1)
        self.u_account = QtWidgets.QLabel(user_profile)
        self.u_account.setObjectName("u_account")
        self.gridLayout.addWidget(self.u_account, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_u_nickname = QtWidgets.QLabel(user_profile)
        self.label_u_nickname.setObjectName("label_u_nickname")
        self.gridLayout.addWidget(self.label_u_nickname, 1, 0, 1, 1)
        self.u_nickname = QtWidgets.QLabel(user_profile)
        self.u_nickname.setObjectName("u_nickname")
        self.gridLayout.addWidget(self.u_nickname, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_u_name = QtWidgets.QLabel(user_profile)
        self.label_u_name.setObjectName("label_u_name")
        self.gridLayout.addWidget(self.label_u_name, 2, 0, 1, 1)
        self.u_name = QtWidgets.QLabel(user_profile)
        self.u_name.setObjectName("u_name")
        self.gridLayout.addWidget(self.u_name, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_u_address1 = QtWidgets.QLabel(user_profile)
        self.label_u_address1.setObjectName("label_u_address1")
        self.horizontalLayout_2.addWidget(self.label_u_address1)
        self.u_address1 = QtWidgets.QTextBrowser(user_profile)
        self.u_address1.setObjectName("u_address1")
        self.horizontalLayout_2.addWidget(self.u_address1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_u_address2 = QtWidgets.QLabel(user_profile)
        self.label_u_address2.setObjectName("label_u_address2")
        self.horizontalLayout.addWidget(self.label_u_address2)
        self.u_address2 = QtWidgets.QTextBrowser(user_profile)
        self.u_address2.setObjectName("u_address2")
        self.horizontalLayout.addWidget(self.u_address2)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 2)
        self.pushButton_edit_profile = QtWidgets.QPushButton(user_profile)
        self.pushButton_edit_profile.setObjectName("pushButton_edit_profile")
        self.gridLayout.addWidget(self.pushButton_edit_profile, 5, 3, 1, 1)
        self.pushButton_buy_membership = QtWidgets.QPushButton(user_profile)
        self.pushButton_buy_membership.setObjectName("pushButton_buy_membership")
        self.gridLayout.addWidget(self.pushButton_buy_membership, 5, 4, 1, 1)
        self.pushButton_logout = QtWidgets.QPushButton(user_profile)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.gridLayout.addWidget(self.pushButton_logout, 5, 5, 1, 1)
        self.label_vip_status = QtWidgets.QLabel(user_profile)
        self.label_vip_status.setObjectName("label_vip_status")
        self.gridLayout.addWidget(self.label_vip_status, 2, 3, 1, 1)
        self.label_u_email = QtWidgets.QLabel(user_profile)
        self.label_u_email.setObjectName("label_u_email")
        self.gridLayout.addWidget(self.label_u_email, 1, 3, 1, 1)
        self.label_u_telephone = QtWidgets.QLabel(user_profile)
        self.label_u_telephone.setObjectName("label_u_telephone")
        self.gridLayout.addWidget(self.label_u_telephone, 0, 3, 1, 1)
        self.u_telephone = QtWidgets.QLabel(user_profile)
        self.u_telephone.setObjectName("u_telephone")
        self.gridLayout.addWidget(self.u_telephone, 0, 4, 1, 1)
        self.u_email = QtWidgets.QLabel(user_profile)
        self.u_email.setObjectName("u_email")
        self.gridLayout.addWidget(self.u_email, 1, 4, 1, 1)
        self.vip_status = QtWidgets.QLabel(user_profile)
        self.vip_status.setObjectName("vip_status")
        self.gridLayout.addWidget(self.vip_status, 2, 4, 1, 1)

        self.retranslateUi(user_profile)
        QtCore.QMetaObject.connectSlotsByName(user_profile)

    def retranslateUi(self, user_profile):
        _translate = QtCore.QCoreApplication.translate
        user_profile.setWindowTitle(_translate("user_profile", "个人信息"))
        self.label_u_account.setText(_translate("user_profile", "用户名："))
        self.u_account.setText(_translate("user_profile", "用户名"))
        self.label_u_nickname.setText(_translate("user_profile", "昵称："))
        self.u_nickname.setText(_translate("user_profile", "昵称"))
        self.label_u_name.setText(_translate("user_profile", "真实姓名："))
        self.u_name.setText(_translate("user_profile", "真实姓名"))
        self.label_u_address1.setText(_translate("user_profile", "收货地址1："))
        self.label_u_address2.setText(_translate("user_profile", "收获地址2："))
        self.pushButton_edit_profile.setText(_translate("user_profile", "编辑个人资料"))
        self.pushButton_buy_membership.setText(_translate("user_profile", "开通/续费会员"))
        self.pushButton_logout.setText(_translate("user_profile", "退出登录"))
        self.label_vip_status.setText(_translate("user_profile", "会员状态："))
        self.label_u_email.setText(_translate("user_profile", "邮箱："))
        self.label_u_telephone.setText(_translate("user_profile", "电话："))
        self.u_telephone.setText(_translate("user_profile", "电话"))
        self.u_email.setText(_translate("user_profile", "邮箱"))
        self.vip_status.setText(_translate("user_profile", "会员状态"))
