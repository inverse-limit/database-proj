import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui_user_profile import *


class user_profile(QtWidgets.QWidget, Ui_user_profile):

    def __init__(self, parent=None):
        super(user_profile, self).__init__(parent)
        self.setupUi(self)