# 数据库类会在controller.py里初始化，然后每个action文件里的类都会有self.database属性就是controller里初始化的数据库对象

class Database:
    pass