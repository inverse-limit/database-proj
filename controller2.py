import sys
from PyQt5.QtWidgets import QApplication
from action_m.action_manage import *
from action.action_detail_search import *
from action_m.action_edit_book_detail import *
from action_m.action_press import *
from action_m.action_press_detail import *
from action_m.action_user_manage import *
from action_m.action_m_user_profile import *
from action_m.action_order_manage import *
from action_m.action_view_cart_order import *
from action_m.action_stat import *

from database import Database


class Controller2:
    def __init__(self):
        # self.database = Database()
        self.database = None

    def show_manage(self):
        self.manage = manage()
        self.manage.database = self.database
        self.manage.switch_detail_research.connect(self.show_detail_search)
        self.manage.switch_book_detail.connect(self.show_book_detail_from_manage)
        self.manage.switch_add_book.connect(self.show_book_detail_add)
        self.manage.switch_press.connect(self.show_press)
        self.manage.switch_user.connect(self.show_user_manage)
        self.manage.switch_order.connect(self.show_order_manage)
        self.manage.put_in_data()
        self.manage.show()

    def show_detail_search(self):
        self.detail_search = detail_research()
        self.detail_search.database = self.database
        self.detail_search.switch_home.connect(self.do_detail_search)
        self.detail_search.show()

    def show_book_detail_from_manage(self):
        self.edit_book_detail = edit_book_detail()
        self.edit_book_detail.database = self.database
        self.edit_book_detail.put_in_data(self.manage.book_id)
        self.edit_book_detail.switch_save.connect(self.refresh_manage)
        self.edit_book_detail.show()

    def show_book_detail_add(self):
        self.edit_book_detail = edit_book_detail()
        self.edit_book_detail.database = self.database
        self.edit_book_detail.put_in_class1()
        self.edit_book_detail.switch_save.connect(self.refresh_manage)
        self.edit_book_detail.show()

    def show_book_detail_from_view(self):
        self.edit_book_detail = edit_book_detail()
        self.edit_book_detail.database = self.database
        self.edit_book_detail.put_in_data(self.view_cart_order.book_id)
        self.edit_book_detail.switch_save.connect(self.refresh_manage)
        self.edit_book_detail.show()

    def show_press(self):
        self.press = press()
        self.press.database = self.database
        self.press.switch_add.connect(self.show_press_detail_add)
        self.press.switch_detail_press.connect(self.show_press_detail)
        self.press.show()

    def show_press_detail(self):
        self.press_detail = press_detail()
        self.press_detail.database = self.database
        self.press_detail.put_in_data(self.press.press_id)
        self.press_detail.switch_save.connect(self.refresh_press)
        self.press_detail.show()

    def show_press_detail_add(self):
        self.press_detail = press_detail()
        self.press_detail.database = self.database
        self.press_detail.switch_save.connect(self.refresh_press)
        self.press_detail.show()

    def show_user_manage(self):
        self.user_manage = user_manage()
        self.user_manage.database = self.database
        self.user_manage.switch_user_profile.connect(self.show_m_user_profile)
        self.user_manage.show()

    def show_m_user_profile(self):
        self.m_user_profile = m_user_profile()
        self.m_user_profile.database = self.database
        self.m_user_profile.put_in_user_data(self.user_manage.user_id)
        self.m_user_profile.switch_order.connect(self.user_order)
        self.m_user_profile.switch_cart.connect(self.user_cart)
        self.m_user_profile.show()

    def show_order_manage(self):
        self.order_manage = order_manage()
        self.order_manage.database = self.database
        self.order_manage.switch_order_detail.connect(self.order_detail)
        self.order_manage.switch_stat.connect(self.show_stat)
        self.order_manage.show()

    def show_stat(self):
        self.stat = statistic()
        self.stat.database = self.database
        self.data = self.order_manage.data
        self.stat.makeup()
        self.stat.show()

    def do_detail_search(self):
        self.manage.detail_search(self.detail_search.search_option)
        self.detail_search.close()

    def refresh_manage(self):
        self.manage.refresh_current_page()
        self.edit_book_detail.close()

    def refresh_press(self):
        self.press.search()
        self.press_detail.close()

    def user_order(self):
        self.order_manage = order_manage()
        self.order_manage.database = self.database
        self.order_manage.lineEdit_search.setText(self.m_user_profile.u_account.text())
        self.order_manage.show()
        self.order_manage.search()

    def user_cart(self):
        self.view_cart_order = view_cart_order()
        self.view_cart_order.database = self.database
        self.view_cart_order.put_in_user_data(user_id = self.m_user_profile.user_id)
        self.view_cart_order.switch_book.connect(self.show_book_detail_from_view)
        self.view_cart_order.show()

    def order_detail(self):
        self.view_cart_order = view_cart_order()
        self.view_cart_order.database = self.database
        self.view_cart_order.put_in_user_data(order_id=self.order_manage.order_id)
        self.view_cart_order.switch_book.connect(self.show_book_detail_from_view)
        self.view_cart_order.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller2()
    main.show_manage()
    sys.exit(app.exec_())