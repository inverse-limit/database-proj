# 数据库类会在controller.py里初始化，然后每个action文件里的类都会有self.database属性就是controller里初始化的数据库对象
import pyodbc

class Database:
    def __init__(self):
       self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=w32s719895.qicp.vip,17865;\
                                   DATABASE=online_bookshop;UID=online_bookshop_m;PWD=dbproject')

    def register_function(self, account, pswd, name, telephone, email, invit, checkpswd):
        cursor = self.cnxn.cursor()
        max0 = cursor.execute("select MAX(u_id) as a from users").fetchone()
        max1 = max0.a + 1
        max0 = cursor.execute("select * from users where u_account = ?", account).fetchone()
        if max0:
            return 0  # 用户名存在
        else:
            if len(account) >10:
                return 6  # 用户名过长
            if len(pswd) < 8:
                return 7  # 密码过短
            if len(pswd) > 10:
                return 8  # 密码过长
            if pswd != checkpswd:
                return 5  # 两次密码不一致
            if invit:
                max0 = cursor.execute("select invtnum from author_book where invtnum = ?", invit).fetchone()
                if max0:
                    cursor.execute("insert into users(u_id,u_account,u_pswd,u_name,u_telephone,u_email,u_invtnum)"
                                   " values(?,?,?,?,?,?,?)",
                                   max1, account, pswd, name, telephone, email, invit)
                    max0 = cursor.execute("select * from users where u_telephone='00000000000'").fetchone()
                    if max0:
                        cursor.execute("delete from users where u_telephone = '00000000000' ")
                        return 3  # 电话不符合格式
                    else:
                        max0 = cursor.execute("select * from users where u_email='11111'").fetchone()
                        if max0:
                            cursor.execute("delete from users where u_email = '11111'")
                            return 4  # 邮箱不符合格式
                        else:
                            cursor.commit()
                            return 2  # 注册成功
                else:
                    return 1  # 邀请码不存在
            else:
                cursor.execute("insert into users(u_id,u_account,u_pswd,u_name,u_telephone,u_email,u_invtnum)"
                               " values(?,?,?,?,?,?,?)",
                               max1, account, pswd, name, telephone, email, invit)
                max0 = cursor.execute("select * from users where u_telephone='00000000000'").fetchone()
                if max0:
                    cursor.execute("delete from users where u_telephone = '00000000000' ")
                    return 3  # 电话不符合格式
                else:
                    max0 = cursor.execute("select * from users where u_email='11111'").fetchone()
                    if max0:
                        cursor.execute("delete from users where u_email = '11111'")
                        return 4  # 邮箱不符合格式
                    else:
                        cursor.commit()
                        return 2  # 注册成功

    def login_check(self, account, pswd):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from users where u_account = ? and u_pswd = ?", account, pswd).fetchone()
        if row:
            return 1
        else:
            return 0

    def login_u_data(self, account, pswd):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from users where u_account = ? and u_pswd = ?", account, pswd).fetchone()
        data = []
        data.append(row.u_account)
        data.append(row.u_nickname)
        data.append(row.u_name)
        data.append(row.u_telephone)
        data.append(row.u_email)
        data.append(row.vip_status)
        data.append(row.u_address1)
        data.append(row.u_address2)
        data.append(row.u_re_time)
        row = cursor.execute("select * from users where u_account = ? and u_pswd = ? and vip_status >= getdate()",
                             account, pswd).fetchone()
        if row:
            data[5] = '会员日期至' + str(row.vip_status)
        else:
            data[5] = '非会员'
        return data

    def home_class(self):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select distinct class1 as a from class").fetchall()
        n = len(row)
        listt = ['...']
        for i in range(0, n):
            listt.append(row[i].a)
        return listt

    def home_class2(self, text):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select distinct subclass as a from class where class1 = ?", text).fetchall()
        n = len(row)
        listt = ['...']
        for i in range(0, n):
            listt.append(row[i].a)
        return listt

    def home_simple_search(self, option, sort):  # ??????
        cursor = self.cnxn.cursor()
        select = "select a.book_id, a.book_name, c.author_name, b.class1 as c, d.press_name, a.reserve, a.on_sale, p.s_price, " \
                 "p.discount, a.mon_sell, a.graph " \
                 "from book a inner join class b on a.book_id=b.book_id " \
                 "inner join author_book c on a.book_id = c.book_id " \
                 "inner join press d on a.press_id = d.press_id " \
                 "inner join price p on a.book_id = p.book_id "
        condition = "where "
        variable = []
        if option[0] != '...':
            condition += "b.class1 = ? and "
            variable.append(option[0])
        if option[1] != '...':
            condition += "b.subclass = ? and "
            variable.append(option[1])
        if option[2]:
            if option[3]:
                condition += "a.book_name like ? and "
                variable.append('%' + option[2] + '%')
            if option[4]:
                condition += "c.author_name like ? and "
                variable.append('%' + option[2] + '%')
        condition += "at = 'a' "
        if sort == '价格升序':
            condition += 'order by p.s_price asc'
        if sort == '价格降序':
            condition += 'order by p.s_price desc'
        if sort == '销量升序':
            condition += 'order by a.mon_sell asc'
        if sort == '销量降序':
            condition += 'order by a.mon_sell desc'
        row = cursor.execute(select + condition, variable).fetchall()
        return row


    def user_accept(self, account, nickname, name, telephone, email, address1, address2):
        cursor = self.cnxn.cursor()
        row = cursor.execute("update users set u_nickname = ?, u_name = ?, u_telephone = ?, u_email = ?,"
                             "u_address1 = ?, u_address2 = ? where u_id = 1", nickname, name, telephone,
                             email, address1, address2)
        check = cursor.execute("select * from users where u_telephone = '00000000000'").fetchone()
        if check:
            cursor.execute("update users set u_telephone = ?, u_email = ? where u_id = 1", '11111111111', '1@f.c')
            cursor.commit()
            return 0  # 电话不符合格式
        else:
            check = cursor.execute("select * from users where u_email = '111111'").fetchone()
            if check:
                cursor.execute("update users set u_telephone = ?, u_email = ? where u_id = 1", '11111111111', '1@f.c')
                cursor.commit()
                return 1  # 邮箱不符合格式
            else:
                cursor.execute("update users set u_nickname = ?, u_name = ?, u_telephone = ?, u_email = ?,"
                             "u_address1 = ?, u_address2 = ? where u_account = ?", nickname, name, telephone,
                             email, address1, address2, account)
                cursor.execute("update users set u_telephone = ?, u_email = ? where u_id = 1", '11111111111', '1@f.c')
                cursor.commit()
                return 2  # 修改成功

    def detail_search(self, bid, bname, a, t, class1, class2, price1, price2, store):
        option = []
        option.append(bid)
        option.append(bname)
        option.append(a)
        option.append(t)
        option.append(class1)
        option.append(class2)
        option.append(price1)
        option.append(price2)
        option.append(store)
        return option

    def home_detail_search(self, option, sort):
        cursor = self.cnxn.cursor()
        select = "select a.book_id, a.book_name, c.author_name, b.class1 as c, d.press_name, a.reserve, a.on_sale, p.s_price, " \
                 "p.discount, a.mon_sell, a.graph " \
                 "from book a inner join class b on a.book_id=b.book_id " \
                 "inner join author_book c on a.book_id = c.book_id " \
                 "inner join press d on a.press_id = d.press_id " \
                 "inner join price p on a.book_id = p.book_id "
        condition = "where "
        variable = []
        if option:
            if option[0]:
                condition += "a.book_id = ? and "
                variable.append(option[0])
            if option[1]:
                condition += "a.book_name like ? and "
                variable.append('%' + option[1] + '%')
            if option[2]:
                condition += "c.author_name = ? and c.at = 'a' and "
                variable.append(option[2])
            if option[3]:
                condition += "c.author_name = ? and c.at = 't' and "
                variable.append(option[3])
            if option[4] != '...':
                condition += "b.class1 = ? and "
                variable.append(option[4])
            if option[5] != '...':
                condition += "b.subclass = ? and "
                variable.append(option[5])
            if option[6]:
                condition += "p.s_price > ? and "
                variable.append(option[6])
            if option[7]:
                condition += "p.s_price < ? and "
                variable.append(option[7])
            if option[8] == '有货':
                condition += "reserve > 0 and "
            else:
                condition += "reserve = 0 and "
            condition += "at = 'a' "
            if sort == '价格升序':
                condition += 'order by p.s_price asc'
            if sort == '价格降序':
                condition += 'order by p.s_price desc'
            if sort == '销量升序':
                condition += 'order by a.mon_sell asc'
            if sort == '销量降序':
                condition += 'order by a.mon_sell desc'
            row = cursor.execute(select + condition, variable).fetchall()
            return row

    def book_detail_putin(self, book_id):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select a.book_id, a.book_name, a.pressdate, c.author_name, d.press_name, "
                             "a.intro, a.graph, a.reserve, p.s_price, p.discount, a.versions "
                             "from book a inner join author_book c on a.book_id = c.book_id "
                             "inner join press d on a.press_id = d.press_id "
                             "inner join price p on a.book_id = p.book_id "
                             "where a.book_id = ? and at = 'a' ", book_id
                             ).fetchone()
        detail = []
        detail.append(row.book_name)
        detail.append(row.author_name)
        detail.append(row.press_name)
        detail.append(row.pressdate)
        detail.append(row.book_id)
        detail.append(row.intro)
        detail.append(row.versions)
        detail.append(row.reserve)
        detail.append(str(row.s_price) + '/' + str(row.discount))
        detail.append(row.graph)
        row = cursor.execute("select a.book_id, a.book_name, a.pressdate, c.author_name, d.press_name, "
                             "a.intro, a.graph "
                             "from book a inner join author_book c on a.book_id = c.book_id "
                             "inner join press d on a.press_id = d.press_id "
                             "where a.book_id = ? and at = 't' ", book_id
                             ).fetchone()
        if row:
            detail[1] += '/' + row.author_name
        return detail

    def cart_select(self, account, vip):
        cursor = self.cnxn.cursor()
        if vip == '非会员':
            row = cursor.execute("select a.cart_id, b.book_name, c.author_name, p.s_price as pr, a.number, b.book_id, b.graph  "
                                 "from cart a inner join book b on a.book_id = b.book_id "
                                 "inner join author_book c on a.book_id = c.book_id "
                                 "inner join price p on a.book_id = p.book_id "
                                 "inner join users u on u.u_id = a.u_id "
                                 "where u.u_account = ?", account).fetchall()
        else:
            row = cursor.execute("select a.cart_id, b.book_name, c.author_name, p.discount as pr, a.number, b.book_id, b.graph "
                                 "from cart a inner join book b on a.book_id = b.book_id "
                                 "inner join author_book c on a.book_id = c.book_id "
                                 "inner join price p on a.book_id = p.book_id "
                                 "inner join users u on u.u_id = a.u_id "
                                 "where u.u_account = ?", account).fetchall()
        return row

    def cart_changenum(self, id, num, vip):
        cursor = self.cnxn.cursor()
        ac = cursor.execute("select u_account from users a "
                            "inner join cart b on a.u_id = b.u_id "
                            "where cart_id = ?", id).fetchone()
        account = ac.u_account
        if num != 0:
            cursor.execute("update cart set number = ? "
                           "where cart_id = ?", num, id)
            cursor.commit()
        else:
            cursor.execute("delete from cart "
                           "where cart_id = ?", id)
            cursor.commit()
        if vip == '非会员':
            row = cursor.execute("select a.cart_id, b.book_name, c.author_name, p.s_price as pr, a.number, b.book_id "
                                 "from cart a inner join book b on a.book_id = b.book_id "
                                 "inner join author_book c on a.book_id = c.book_id "
                                 "inner join price p on a.book_id = p.book_id "
                                 "inner join users u on u.u_id = a.u_id "
                                 "where u.u_account = ?", account).fetchall()
        else:
            row = cursor.execute("select a.cart_id, b.book_name, c.author_name, p.discount as pr, a.number, b.book_id "
                                 "from cart a inner join book b on a.book_id = b.book_id "
                                 "inner join author_book c on a.book_id = c.book_id "
                                 "inner join price p on a.book_id = p.book_id "
                                 "inner join users u on u.u_id = a.u_id "
                                 "where u.u_account = ?", account).fetchall()
        return row

    def cart_book_detail(self, cid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from cart where cart_id = ?", cid).fetchone()
        return row

    def isorder(self, odata):
        cursor = self.cnxn.cursor()
        n = len(odata)
        for i in range(0, n):
            num0 = cursor.execute("select reserve from book where book_id = ?", odata[i].book_id).fetchone()
            num1 = num0.reserve
            if num1 < odata[i].number:
                return odata[i].book_name

    def order_ok(self, udata, odata):
        cursor = self.cnxn.cursor()
        max0 = cursor.execute("select max(sell_id) as m from sell").fetchone()
        u_id0 = cursor.execute("select u_id from users where u_account = ?", udata[0]).fetchone()
        idd = u_id0.u_id
        if max0.m:
            max1 = max0.m + 1
        else:
            max1 = 1
        max0 = cursor.execute("select max(sb_id) as m from sell_book").fetchone()
        if max0.m:
            max2 = max0.m + 1
        else:
            max2 = 1
        n = len(odata)
        total = 0
        for i in range(0, n):
            total += odata[i].pr * odata[i].number
        cursor.execute("insert into sell values(?,getdate(),?,?)", max1, idd, total)
        cursor.commit()
        for i in range(0, n):
            cursor.execute("insert into sell_book values(?,?,?,?,?)",
                           max2, max1, odata[i].book_id, odata[i].pr, odata[i].number)
            cursor.commit()
            max2 += 1
        for i in range(0, n):
            cc = cursor.execute("select cart_id, number from cart where u_id = ? and book_id = ?",
                                idd, odata[i].book_id).fetchone()
            cid = cc.cart_id
            tnum = cc.number
            if tnum - odata[i].number != 0:
                cursor.execute("update cart set number = ? "
                               "where cart_id = ?", tnum - odata[i].number, cid)
                cursor.commit()
            else:
                cursor.execute("delete from cart "
                               "where cart_id = ?", cid)
                cursor.commit()
            cursor.execute("update book set mon_sell = mon_sell + ? where book_id = ?",
                           odata[i].number, odata[i].book_id)
            cursor.commit()
            cursor.execute("update book set reserve = reserve - ? where book_id = ?",
                           odata[i].number, odata[i].book_id)

    def add_cart(self, bid, account, vip):
        cursor = self.cnxn.cursor()
        max0 = cursor.execute("select max(cart_id) as m from cart").fetchone()
        if max0.m:
            max1 = max0.m+1
        else:
            max1 = 1
        id0 = cursor.execute("select u_id from users where u_account  = ?", account).fetchone()
        id1 = id0.u_id
        if vip == '非会员':
            row = cursor.execute("select s_price from price where book_id = ?", bid).fetchone()
            pr = row.s_price
        else:
            row = cursor.execute("select discount from price where book_id = ?", bid).fetchone()
            pr = row.discount
        cursor.execute("insert into cart values(?,?,?,?,1)", max1, id1, bid, pr)
        cursor.commit()

    def manage_simple_search(self, option, filter, sort):  # ??????
        cursor = self.cnxn.cursor()
        select = "select a.book_id, a.book_name, c.author_name, b.class1 as c, d.press_name, a.reserve, a.on_sale, p.s_price, " \
                 "p.discount, a.mon_sell, a.graph " \
                 "from book a inner join class b on a.book_id=b.book_id " \
                 "inner join author_book c on a.book_id = c.book_id " \
                 "inner join press d on a.press_id = d.press_id " \
                 "inner join price p on a.book_id = p.book_id "
        condition = "where "
        variable = []
        if option[0] != '...':
            condition += "b.class1 = ? and "
            variable.append(option[0])
        if option[1] != '...':
            condition += "b.subclass = ? and "
            variable.append(option[1])
        if option[2]:
            if option[3]:
                condition += "a.book_name like ? "
                variable.append('%' + option[2] + '%')
            if option[4]:
                condition += "c.author_name like ? "
                variable.append('%' + option[2] + '%')
        if filter == '已上架':
            condition += "on_sale = 'on' and "
        if filter == '未上架':
            condition += "on_sale = 'off' and "
        condition += "at = 'a' "
        if sort == '价格升序':
            condition += 'order by p.s_price asc'
        if sort == '价格降序':
            condition += 'order by p.s_price desc'
        if sort == '销量升序':
            condition += 'order by a.mon_sell asc'
        if sort == '销量降序':
            condition += 'order by a.mon_sell desc'
        row = cursor.execute(select + condition, variable).fetchall()
        return row

    def manage_detail_search(self, option, filter, sort):
        cursor = self.cnxn.cursor()
        select = "select a.book_id, a.book_name, c.author_name, b.class1 as cl, d.press_name, a.reserve, a.on_sale, p.s_price, " \
                 "p.discount, a.mon_sell, a.graph "\
                 "from book a inner join class b on a.book_id=b.book_id " \
                 "inner join author_book c on a.book_id = c.book_id " \
                 "inner join press d on a.press_id = d.press_id " \
                 "inner join price p on a.book_id = p.book_id "
        condition = "where "
        variable = []
        if option:
            if option[0]:
                condition += "a.book_id = ? and "
                variable.append(option[0])
            if option[1]:
                condition += "a.book_name like ? and "
                variable.append('%' + option[1] + '%')
            if option[2]:
                condition += "c.author_name = ? and c.at = 'a' and "
                variable.append(option[2])
            if option[3]:
                condition += "c.author_name = ? and c.at = 't' and "
                variable.append(option[3])
            if option[4] != '...':
                condition += "b.class1 = ? and "
                variable.append(option[4])
            if option[5] != '...':
                condition += "b.subclass = ? and "
                variable.append(option[5])
            if option[6]:
                condition += "p.s_price > ? and "
                variable.append(option[6])
            if option[7]:
                condition += "p.s_price < ? and "
                variable.append(option[7])
            if option[8] == '有货':
                condition += "reserve > 0 and "
            else:
                condition += "reserve = 0 and "
            if filter == '已上架':
                condition += "on_sale = 'on' and "
            if filter == '未上架':
                condition += "on_sale = 'off' and "
            condition += "at = 'a' "
            if sort == '价格升序':
                condition += 'order by p.s_price asc'
            if sort == '价格降序':
                condition += 'order by p.s_price desc'
            if sort == '销量升序':
                condition += 'order by a.mon_sell asc'
            if sort == '销量降序':
                condition += 'order by a.mon_sell desc'
            row = cursor.execute(select + condition, variable).fetchall()
            return row

    def manage_on_off_de_book(self, blist, sta):
        cursor = self.cnxn.cursor()
        n = len(blist)
        if sta == 'down':
            stat = 'off'
        if sta == 'up':
            stat = 'on'
        for i in range(0, n):
            cursor.execute("update book set on_sale = ? whrere book_id = ?", stat, blist[i])
            cursor.commit()
        if sta == 'delete':
            for i in range(0, n):
                cursor.execute("delete from book whrere book_id = ?", blist[i])
                cursor.commit()

    def m_user_manage_search(self, option):
        cursor = self.cnxn.cursor()
        select = "select * from users "
        condition = "where "
        variable = []
        if option[0]:
            if option[1]:
                condition += "u_account = ? and "
                variable.append(option[0])
            if option[2]:
                condition += "u_nickname like ? and "
                variable.append('%' + option[0] + '%')
        if option[5] == '非会员':
            condition += "(vip_status < getdate() or vip_status = NULL) and "
        if option[5] == '会员':
            condition += "vip_status >= getdate() and "
        if option[5] == '作家用户':
            condition += "u_invtnum != NULL and "
        condition += "u_re_time >= ? and u_re_time <= ? "
        variable.append(option[3])
        variable.append(option[4])
        row = cursor.execute(select + condition, variable).fetchall()
        return row

    def m_user_profile(self, uid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from users where u_id = ? ", uid).fetchone()
        return row

    def m_order_manage_search(self, option):
        cursor = self.cnxn.cursor()
        select = "select * from users a inner join sell b on a.u_id = b.u_id "\
                 "inner join sell_book c on b.sell_id = c.sell_id "
        condition = "where "
        variable = []
        if option[0]:
            if option[1]:
                condition += "u_account = ? and "
                variable.append(option[0])
            if option[2]:
                condition += "u_nickname = ? and "
                variable.append(option[0])
        condition += "s_date >= ? and s_date <= ? order by b.sell_id"
        variable.append(option[3])
        variable.append(option[4])
        row = cursor.execute(select + condition, variable).fetchall()
        sell_id = cursor.execute("select distinct b.sell_id from users a inner join sell b on a.u_id = b.u_id "
                                 "inner join sell_book c on b.sell_id = c.sell_id " + condition, variable).fetchall()
        return [row, sell_id]

    def m_press_search(self, option):
        cursor = self.cnxn.cursor()
        select = "select * from press "
        condition = "where "
        variable = []
        if option[0]:
            if option[1]:
                condition += "press_name like ? "
                variable.append('%' + option[0] + '%')
            if option[2]:
                condition += "person like ? "
                variable.append('%' + option[0] + '%')
            row = cursor.execute(select + condition, variable).fetchall()
            return row
        else:
            row = cursor.execute("select * from press").fetchall()
            return row

    def m_press_detail(self, pid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from press where press_id = ? ", pid).fetchone()
        return row

    def m_press_save(self, pid, option):
        cursor = self.cnxn.cursor()
        if len(option[0]) == 0:
            return 0
        if len(option[1]) == 0:
            return 1
        if len(option[2]) == 0:
            return 2
        if len(option[3]) == 0:
            return 3
        if len(option[4]) == 0:
            return 4
        if pid:
            cursor.execute("update press set press_name = ?, person = ?, telephone = ?, "
                           "email = ?, address = ? where press_id = ?", option[0], option[1],
                           option[2], option[3], option[4], pid)
            cursor.commit()
        else:
            max0 = cursor.execute("select max(press_id) as m from press").fetchone()
            if max0:
                max1 = max0.m + 1
            else:
                max1 = 1
            cursor.execute("insert into press values(?, ?, ?, ?, ?, ?)", max1, option[0], option[1],
                           option[2], option[3], option[4])
            cursor.commit()
        return 5

    def m_cart_view_u(self, uid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from users a inner join cart b on a.u_id = b.u_id "
                             "inner join book c on b.book_id = c.book_id "
                             "inner join author_book d on c.book_id = d.book_id "
                             "where a.u_id = ? and at = 'a'", uid).fetchall()
        return row

    def m_order_view(self, sid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from users a inner join sell b on a.u_id = b.u_id "
                             "inner join sell_book c on b.sell_id = c.sell_id "
                             "inner join book d on c.book_id = d.book_id "
                             "inner join author_book e on d.book_id = e.book_id "
                             "where b.sell_id = ? and at = 'a'", sid).fetchall()
        return row

    def m_book_detail(self, bid):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from book a inner join author_book b on a.book_id = b.book_id "
                             "inner join press c on a.press_id = c.press_id "
                             "inner join price d on a.book_id = d.book_id "
                             "inner join class e on a.book_id = e.book_id "
                             "where at = 'a'").fetchone()
        row1 = cursor.execute("select * from book a inner join author_book b on a.book_id = b.book_id "
                              "inner join press c on a.press_id = c.press_id "
                              "inner join price d on a.book_id = d.book_id "
                              "inner join class e on a.book_id = e.book_id "
                              "where at = 't'").fetchone()
        return [row, row1]

    def update_book(self, bid, option):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from press where press_name = ?", option[3]).fetchone()
        if row:
            press_id = row.press_id
            update = "update book set book_name = ?, press_id = ?, pressdate = ?, " \
                     "versions = ?, reserve = 0 "
            if option[0] is None or len(option[0]) == 0:
                return 3  # 未填写书名
            if option[8] is None or len(option[8]) == 0 or option[8] != bid:
                return 4  # ISBN不可修改
            if option[9] is None or len(str(option[9])) == 0:
                return 5  # 未填写出版日期
            if option[10] is None:
                return 6  # 未填写版本号
            variable = [option[0], press_id, option[9], option[10]]
            if option[13]:
                update += ", intro = ? "
                variable.append(option[13])
            variable.append(bid)
            cursor.execute(update + "where book_id = ?", variable)
            if option[1]:
                cursor.execute("update author_book set author_name = ? where book_id = ? and "
                               "at = 'a'", option[1], bid)
                if option[2]:
                    row = cursor.execute("select * from author_book where book_id = ? and at = 't'",
                                         bid).fetchone()
                    if row:
                        cursor.execute("update author_book set author_name = ? where book_id = ? "
                                       "and at = 't'", option[2])
                    else:
                        max0 = cursor.execute("select max(ab_id) as m from author_book").fetchone()
                        if max0:
                            max1 = max0.m + 1
                        else:
                            max1 = 1
                        cursor.execute("insert into author_book values(?,?,?,'t')", max1, option[2], bid)
                else:
                    row = cursor.execute("select * from author_book where book_id = ? and at = 't'",
                                         bid).fetchone()
                    if row:
                        cursor.execute("delete from author_book where author_name = ? and book_id = ? "
                                       "and at = 't'", option[2])
                if option[6]:
                    if option[7]:
                        cursor.execute("update class set class1 = ?, subclass = ? where book_id = ?", option[6], option[7], bid)
                    else:
                        cursor.execute("update class set class1 = ? where book_id = ?", option[6], bid)
                else:
                    if option[4] == '...':
                        return 8
                    else:
                        if option[5] != '...':
                            cursor.execute("update class set class1 = ?, subclass = ? where book_id = ?", option[4], option[5], bid)
                        else:
                            cursor.execute("update class set class1 = ? where book_id = ?", option[4], bid)
                if option[11]:
                    if option[12]:
                        cursor.execute("update price set s_price = ?, discount = ? where book_id = ?", option[11], option[12], bid)
                    else:
                        cursor.execute("update price set s_price = ?, discount = ? where book_id = ?", option[11], option[11], bid)
                    cursor.commit()
                    return -1  #保存成功
                else:
                    return 2  # 未填写单价
            else:
                return 1  # 未填写作者
        else:
            return 0  # 出版社不存在 请先添加出版社信息

    def insert_book(self, option):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select * from press where press_name = ?", option[3]).fetchone()
        if row:
            press_id = row.press_id
            if option[0] is None or len(option[0]) == 0:
                return 3  # 未填写书名
            if option[8] is None or len(option[8]) == 0:
                return 4  # 未填写ISBN
            if option[9] is None or len(str(option[9])) == 0:
                return 5  # 未填写出版日期
            if option[10] is None or len(option[10]) == 0:
                return 6  # 未填写版本号
            row = cursor.execute("select * from book where book_id = ?", option[8]).fetchone()
            if row:
                return 7  # ISBN已存在
            cursor.execute("insert into book(book_id, book_name, press_id, pressdate, versions, reserve)"
                           " values(?, ?, ?, ?, ?, 0)", option[8], option[0], press_id, option[9], option[10])
            if option[13]:
                cursor.execute("update book set intro = ? where book_id = ?", option[13], option[8])
            if option[1]:
                max0 = cursor.execute("select max(ab_id) from author_book").fetchval()
                cursor.execute("insert into author_book(ab_id, author_name, book_id, at) values(?,?,?,'a')", max0 + 1, option[1], option[8])
                if option[2]:
                    max0 = cursor.execute("select max(ab_id) from author_book").fetchval()
                    cursor.execute("insert into author_book(ab_id, author_name, book_id, at) values(?,?,?,'t')", max0 + 1, option[2], option[8])
                if option[6]:
                    max0 = cursor.execute("select max(class_id) from class").fetchval()
                    if option[7]:
                        cursor.execute("insert into class values(?,?,?,?)", max0 + 1, option[8], option[6], option[7])
                    else:
                        cursor.execute("insert into class(class_id, book_id, class1)"
                                       " values(?,?,?)", max0 + 1, option[8], option[6])
                else:
                    if option[4] == '...':
                        return 8  # 请填写新建类别或选择分类
                    max0 = cursor.execute("select max(class_id) from class").fetchval()
                    if option[5] != '...':
                        cursor.execute("insert into class values(?,?,?,?)", max0 + 1 , option[8], option[4], option[5])
                    else:
                        cursor.execute("insert into class(class_id, book_id, class1) values(?, ?, ?)", max0+1, option[8], option[4])
                if option[11]:
                    if option[12]:
                        cursor.execute("insert into price values(?,?,?)", option[8], option[11], option[12])
                    else:
                        cursor.execute("insert into price(book_id, s_price) values(?,?)", option[8], option[11])
                    cursor.commit()
                    return -1  #保存成功
                else:
                    return 2  # 未填写单价
            else:
                return 1  # 未填写作者
        else:
            return 0  # 出版社不存在 请先添加出版社信息

    def his_order(self, account, flag, d1, d2):
        if flag == 'no':
            cursor = self.cnxn.cursor()
            select = "select * from users a inner join sell b on a.u_id = b.u_id " \
                     "inner join sell_book c on b.sell_id = c.sell_id "
            condition = "where u_account = ?"
            row = cursor.execute(select + condition, account).fetchall()
            sell_id = cursor.execute("select distinct b.sell_id from users a inner join sell b on a.u_id = b.u_id "
                                     "inner join sell_book c on b.sell_id = c.sell_id " + condition,
                                     account).fetchall()
            return [row, sell_id]
        if flag == 'yes':
            cursor = self.cnxn.cursor()
            select = "select * from users a inner join sell b on a.u_id = b.u_id " \
                     "inner join sell_book c on b.sell_id = c.sell_id "
            condition = "where "
            variable = []
            condition += "s_date >= ? and s_date <= ? order by b.sell_id"
            variable.append(d1)
            variable.append(d2)
            row = cursor.execute(select + condition, variable).fetchall()
            sell_id = cursor.execute("select distinct b.sell_id from users a inner join sell b on a.u_id = b.u_id "
                                     "inner join sell_book c on b.sell_id = c.sell_id " + condition,
                                     variable).fetchall()
            return [row, sell_id]

    def buy_vip(self, account, option):
        cursor = self.cnxn.cursor()
        d =cursor.execute("select * from users where vip_status >= getdate() and u_account = ? ", account).fetchone()
        a = 0
        if option[0]:
            a = 1
        if option[1]:
            a = 3
        if option[2]:
            a = 6
        if option[3]:
            a = 12
        if a != 0:
            if d:
                cursor.execute("update users set vip_status = dateadd(m, ?, ?) where u_account = ?", a, d.vip_status, account)
                cursor.commit()
            else:
                cursor.execute("update users set vip_status = dateadd(m, ?, getdate()) where u_account = ?", a, account)
                cursor.commit()
            row = cursor.execute("select vip_status from users where u_account = ?", account).fetchone()
            return row