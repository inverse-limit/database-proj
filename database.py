# 数据库类会在controller.py里初始化，然后每个action文件里的类都会有self.database属性就是controller里初始化的数据库对象
import pyodbc

class Database:
    def __init__(self):
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.102;\
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
                return 6  # 过长
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
        row = cursor.execute("select * from users where u_account = ? and u_pswd = ? and vip_status > getdate()",
                             account, pswd).fetchone()
        if row:
            data[5] = '会员日期至' + str(row.vip_status)
        else:
            data[5] = '非会员'
        return data

    def home_class(self):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select distinct class as a from class").fetchall()
        n = len(row)
        listt = ['...']
        for i in range(0, n):
            listt.append(row[i].a)
        return listt

    def home_class2(self, text):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select distinct subclass as a from class where class = ?", text).fetchall()
        n = len(row)
        listt = ['...']
        for i in range(0, n):
            listt.append(row[i].a)
        return listt

    def home_simple_search(self, option):   #??????
        cursor = self.cnxn.cursor()
        if option[2]:
            if option[0] != '...':
                if option[3]:
                    if option[1] != '...':
                        row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                             "p.s_price, a.mon_sell, a.reserve "
                                             "from book a inner join class b on a.book_id=b.book_id "
                                             "inner join author_book c on a.book_id = c.book_id "
                                             "inner join press d on a.press_id = d.press_id "
                                             "inner join price p on a.book_id = p.book_id "
                                             "where b.class = ? and b.subclass = ? and a.book_name like ? ",
                                             option[0], option[1], '%'+option[2]+'%').fetchall()
                        return row
                    else:
                        row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                             "p.s_price, a.mon_sell, a.reserve "
                                             "from book a inner join class b on a.book_id=b.book_id "
                                             "inner join author_book c on a.book_id = c.book_id "
                                             "inner join press d on a.press_id = d.press_id "
                                             "inner join price p on a.book_id = p.book_id "
                                             "where b.class = ? and a.book_name like ? ",
                                             option[0], '%' + option[2] + '%').fetchall()
                        return row
                if option[4]:
                    if option[1] != '...':
                        row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                             "p.s_price, a.mon_sell, a.reserve "
                                             "from book a inner join class b on a.book_id=b.book_id "
                                             "inner join author_book c on a.book_id = c.book_id "
                                             "inner join press d on a.press_id = d.press_id "
                                             "inner join price p on a.book_id = p.book_id "
                                             "where b.class = ? and b.subclass = ? and c.author_name like ? ",
                                             option[0], option[1], '%' + option[2] + '%').fetchall()
                        return row
                    else:
                        row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                             "p.s_price, a.mon_sell, a.reserve "
                                             "from book a inner join class b on a.book_id=b.book_id "
                                             "inner join author_book c on a.book_id = c.book_id "
                                             "inner join press d on a.press_id = d.press_id "
                                             "inner join price p on a.book_id = p.book_id "
                                             "where b.class = ? and c.author_name like ? ",
                                             option[0], '%' + option[2] + '%').fetchall()
                        return row
            if option[0] == '...':
                if option[3]:
                    row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                         "p.s_price, a.mon_sell, a.reserve "
                                         "from book a inner join class b on a.book_id=b.book_id "
                                         "inner join author_book c on a.book_id = c.book_id "
                                         "inner join press d on a.press_id = d.press_id "
                                         "inner join price p on a.book_id = p.book_id "
                                         "where a.book_name like ? ",
                                         '%' + option[2] + '%').fetchall()
                    return row
                if option[4]:
                    row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                         "p.s_price, a.mon_sell, a.reserve "
                                         "from book a inner join class b on a.book_id=b.book_id "
                                         "inner join author_book c on a.book_id = c.book_id "
                                         "inner join press d on a.press_id = d.press_id "
                                         "inner join price p on a.book_id = p.book_id "
                                         "where c.author_name like ? ",
                                         '%' + option[2] + '%').fetchall()
                    return row
        if option[0]:
            if option[1] != '...':
                row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                     "p.s_price, a.mon_sell, a.reserve "
                                     "from book a inner join class b on a.book_id=b.book_id "
                                     "inner join author_book c on a.book_id = c.book_id "
                                     "inner join press d on a.press_id = d.press_id "
                                     "inner join price p on a.book_id = p.book_id "
                                     "where b.class = ? and b.subclass = ?",
                                     option[0], option[1]).fetchall()
                return row
            else:
                row = cursor.execute("select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "
                                     "p.s_price, a.mon_sell, a.reserve "
                                     "from book a inner join class b on a.book_id=b.book_id "
                                     "inner join author_book c on a.book_id = c.book_id "
                                     "inner join press d on a.press_id = d.press_id "
                                     "inner join price p on a.book_id = p.book_id "
                                     "where b.class = ?", option[0]).fetchall()
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

    def detail_search_result(self, option):
        cursor = self.cnxn.cursor()
        select = "select a.book_id, a.book_name, c.author_name, b.class as c, d.press_name, "\
                 "p.s_price, a.mon_sell, a.reserve " \
                 "from book a inner join class b on a.book_id=b.book_id "\
                 "inner join author_book c on a.book_id = c.book_id "\
                 "inner join press d on a.press_id = d.press_id "\
                 "inner join price p on a.book_id = p.book_id "
        condition = "where "
        variable = []
        if option:
            if option[0]:
                condition += "a.book_id = ? and "
                variable.append(option[0])
            if option[1]:
                condition += "a.book_name = ? and "
                variable.append(option[1])
            if option[2]:
                condition += "c.author_name = ? and c.at = 'a' and "
                variable.append(option[2])
            if option[3]:
                condition += "c.author_name = ? and c.at = 't' and "
                variable.append(option[3])
            if option[4]:
                condition += "b.class = ? and "
                variable.append(option[4])
            if option[5]:
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
            condition += "p.s_price>0"
            row = cursor.execute(select + condition, variable).fetchall()
            return row

    def book_detail_putin(self, book_id):
        cursor = self.cnxn.cursor()
        row = cursor.execute("select a.book_id, a.book_name, a.pressdate, c.author_name, d.press_name, "
                             "a.intro, a.graph "
                             "from book a inner join author_book c on a.book_id = c.book_id "
                             "inner join press d on a.press_id = d.press_id "
                             "where a.book_id = ?", book_id
                             ).fetchone()
        detail = []
        detail.append(row.book_name)
        detail.append(row.author_name)
        detail.append(row.press_name)
        detail.append(row.pressdate)
        detail.append(row.book_id)
        detail.append(row.intro)
        detail.append(row.graph)
        return detail

    def cart_select(self, account, vip):
        cursor = self.cnxn.cursor()
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