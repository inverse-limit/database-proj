import sys
from PyQt5.QtWidgets import QApplication
from action_login_window import *
from action_register_window import *


class Controller:
    def __init__(self):
        pass

    def show_login_window(self):
        self.login = login_window()
        self.login.switch_register.connect(self.show_register_window)
        self.login.show()

    def show_register_window(self):
        self.register = register_window()
        self.register.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller()
    main.show_login_window()
    sys.exit(app.exec_())