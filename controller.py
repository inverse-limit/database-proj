import sys
from PyQt5.QtWidgets import QApplication
from action.action_login_window import *
from action.action_register_window import *
from action.action_home_window import *
from action.action_detail_search import *
from action.action_user_profile import *
from action.action_cart import *
from action.action_book_detail import *
from action.action_user_order import *
from action_m.action_view_cart_order import *

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
        self.home.put_in_data()
        self.home.switch_detail_research.connect(self.show_detail_search)
        self.home.switch_contactus.connect(self.show_contactus)
        self.home.switch_user_profile.connect(self.show_user_profile)
        self.home.switch_book_detail.connect(self.show_book_detail)
        self.home.switch_cart.connect(self.show_cart)
        self.home.switch_user_order.connect(self.show_user_order)
        self.home.show()

    def show_user_order(self):
        self.user_order = user_order()
        self.user_order.database = self.database
        self.user_order.put_in_data(self.home.user_data)
        self.user_order.switch_view.connect(self.show_view)
        self.user_order.show()

    def show_view(self):
        self.view = view_cart_order()
        self.view.database = self.database
        self.view.put_in_user_data(order_id=self.user_order.order_id)
        self.view.show()

    def show_detail_search(self):
        self.detail_search = detail_research()
        self.detail_search.database = self.database
        self.detail_search.put_in_data()
        self.detail_search.switch_home.connect(self.do_detail_search)
        self.detail_search.show()

    def show_user_profile(self):  # user_profile类的个人信息由home的user_data传入
        self.user_profile = user_profile()
        self.user_profile.database = self.database
        self.user_profile.put_in_user_data(self.home.user_data)
        self.user_profile.switch_edit_profile.connect(self.show_edit_user_profile)
        self.user_profile.switch_buy_vip.connect(self.show_buy_vip)
        self.user_profile.switch_login.connect(self.logout)
        self.user_profile.show()

    def logout(self):
        self.user_profile.close()
        try:
            self.home.close()
        except:
            pass
        self.show_login_window()

    def show_buy_vip(self):
        self.buy_vip = buy_vip()
        self.buy_vip.database = self.database
        self.buy_vip.switch_user_profile.connect(self.refresh_user_profile)
        self.buy_vip.user_data = self.home.user_data
        self.buy_vip.show()

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
        self.cart.switch_confirm_order.connect(self.show_confirm_order)
        self.cart.switch_book_detail.connect(self.show_book_detail_from_cart)
        self.cart.refresh_cart(self.home.user_data)
        self.cart.show()

    def show_confirm_order(self):
        self.confirm_order = confirm_order()
        self.confirm_order.database = self.database
        self.confirm_order.total_price = self.cart.price.text()
        self.confirm_order.put_in_data(self.home.user_data, self.cart.cart_content, self.cart.select_list)
        self.confirm_order.switch_cart.connect(self.end_buy)
        self.confirm_order.show()

    def show_book_detail(self):
        self.book_detail = book_detail()
        self.book_detail.database = self.database
        self.book_detail.switch_cart.connect(self.add_to_cart)
        self.book_detail.user_data = self.home.user_data
        self.book_detail.put_in_data(self.home.book_id)
        self.book_detail.show()

    def show_book_detail_from_cart(self):
        self.book_detail = book_detail()
        self.book_detail.database = self.database
        self.book_detail.switch_cart.connect(self.add_to_cart)
        self.book_detail.user_data = self.home.user_data
        self.book_detail.put_in_data(self.cart.book_id)
        self.book_detail.show()


    def show_contactus(self):
        pass

    def refresh_user_profile(self):
        self.home.user_data = self.buy_vip.user_data
        self.user_profile.close()
        self.show_user_profile()

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

    def add_to_cart(self):
        try:
            self.cart.refresh_cart(self.home.user_data)
        except:
            pass

    def end_buy(self):
        try:
            self.cart.refresh_cart(self.home.user_data)
        except:
            pass
        self.confirm_order.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller()
    main.show_login_window()
    sys.exit(app.exec_())