import sys
from PyQt5.QtWidgets import QApplication
from action.action_login_window import *
from action.action_register_window import *
from action.action_home_window import *
from action.action_detail_search import *
from action.action_user_profile import *
from action.action_cart import *

from database import Database


class Controller:
    def __init__(self):
        self.database = Database()

    def show_login_window(self):
        self.login = login_window()
        self.login.database = self.database
        self.login.switch_register.connect(self.show_register_window)
        self.login.switch_home.connect(self.show_home_window)
        self.login.show()

    def show_register_window(self):
        self.register = register_window()
        self.register.database = self.database
        self.register.show()

    def show_home_window(self):
        self.login.close()
        self.home = home_window()
        self.home.database = self.database
        self.home.user_data = self.login.user_data
        self.home.switch_detail_research.connect(self.show_detail_search)
        self.home.switch_contactus.connect(self.show_contactus)
        self.home.switch_user_profile.connect(self.show_user_profile)
        self.home.switch_cart.connect(self.show_cart)
        self.home.show()

    def show_detail_search(self):
        self.detail_search = detail_research()
        self.detail_search.database = self.database
        self.detail_search.switch_home.connect(self.do_detail_search)
        self.detail_search.show()

    def show_user_profile(self):  # user_profile类的个人信息由home的user_data传入
        self.user_profile = user_profile()
        self.user_profile.database = self.database
        self.user_profile.put_in_user_data(self.home.user_data)
        self.user_profile.switch_edit_profile.connect(self.show_edit_user_profile)
        self.user_profile.show()

    def show_edit_user_profile(self):
        self.edit_user_profile = edit_user_profile()
        self.edit_user_profile.database = self.database
        self.edit_user_profile.put_in_user_data(self.home.user_data)
        self.edit_user_profile.switch_user_profile_accept.connect(self.edit_user_profile_accept)
        self.edit_user_profile.switch_user_profile_cancel.connect(self.edit_user_profile_cancel)
        self.user_profile.close()
        self.edit_user_profile.show()

    def show_cart(self):
        self.cart = cart()
        self.cart.database = self.database
        self.cart_isopen = True
        self.cart.switch_confirm_order.connect(self.show_confirm_order)
        self.cart.show()
        self.cart.refresh_cart(self.home.user_data)

    def show_confirm_order(self):
        self.confirm_order = confirm_order()
        self.confirm_order.database = self.database
        self.confirm_order.show()

    def show_contactus(self):
        pass

    def do_detail_search(self):
        self.home.detail_search(self.detail_search.search_option)
        self.detail_search.close()

    def edit_user_profile_accept(self):  # 修改个人信息保存 更新home类的个人信息 重新初始化user_profile类并打开
        self.home.user_data = self.edit_user_profile.user_data
        self.edit_user_profile.close()
        self.show_user_profile()

    def edit_user_profile_cancel(self):
        self.edit_user_profile.close()
        self.show_user_profile()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller()
    main.show_login_window()
    sys.exit(app.exec_())