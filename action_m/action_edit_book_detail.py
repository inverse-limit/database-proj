import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from ui.ui_edit_book_detail import *


class edit_book_detail(QtWidgets.QWidget, Ui_edit_book_detail):
    switch_save = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(edit_book_detail, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_upload.clicked.connect(self.upload_cover)
        self.comboBox_class1.activated[str].connect(self.get_class2)
        self.book_id = None

    def put_in_class1(self):
        """
        TODO:往类别1里填默认的类别，和manage一样 这里不需要 ... 项
             class2里填默认类别对应的子类别
        """

    def get_class2(self, text):
        """
        TODO:根据class1往class2里填类别，和manage一样 这里不需要 ... 项
        """

    def put_in_data(self, book_id=None):
        if book_id:
        # TODO:利用book_id调出图书信息，
        #      填到界面里，并且存到self.book_id里，intro还是intro，其它前面加个lineEdit比如lineEdit_book_name
            # 封面加入方法
            # path = './icon/test_pic2'
            # self.picture.setPixmap(QtGui.QPixmap(path))
            pass

    def save(self):
        """
        TODO:如果self.book_id不为None, 说明是双击表格进来的，把对书详细信息的改动保存到数据库
             如果self.book_id为None,说明是新增书目进来的，检验下除了简介封面译者以外的格子是不是都填了
             然后把新书的信息放到数据库，默认是未上架状态
        """
        self.switch_save.emit()

    def upload_cover(self):
        img = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', './', '图像文件 (*.jpg *.png)')[0]  # 选取文件 返回文件路径
        # TODO:把文件上传服务器和书对应起来
        self.picture.setPixmap(QtGui.QPixmap(img))  # 把图片放进画面里