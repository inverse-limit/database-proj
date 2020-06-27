import sys
from PyQt5.QtWidgets import QApplication
from action_login_window import *
from action_register_window import *
from action_home_window import *
from action_detail_search import *
from action_user_profile import *


class Controller:
    def __init__(self):
        pass

    def show_login_window(self):
        self.login = login_window()
        self.login.switch_register.connect(self.show_register_window)
        self.login.switch_home.connect(self.show_home_window)
        self.login.show()

    def show_register_window(self):
        self.register = register_window()
        self.register.show()

    def show_home_window(self):
        self.login.close()
        self.home = home_window()
        self.home.switch_detail_research.connect(self.show_detail_search)
        self.home.switch_contactus.connect(self.show_contactus)
        self.home.switch_user_profile.connect(self.show_user_profile)
        self.home.show()

    def show_detail_search(self):
        self.detail_search = detail_research()
        self.detail_search.show()

    def show_user_profile(self):
        self.user_profile = user_profile()
        self.user_profile.show()

    def show_contactus(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller()
    main.show_login_window()
    sys.exit(app.exec_())