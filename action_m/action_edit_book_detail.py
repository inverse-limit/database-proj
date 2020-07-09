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
        listt = self.database.home_class()
        self.comboBox_class1.addItems(listt)

    def get_class2(self, text):
        """
        TODO:根据class1往class2里填类别，和manage一样 这里不需要 ... 项
        """
        self.comboBox_class2.clear()
        listt = self.database.home_class2(text)
        self.comboBox_class2.addItems(listt)

    def put_in_data(self, book_id=None):
        if book_id:
            self.book_id = book_id
            self.row = self.database.m_book_detail(book_id)
            self.lineEdit_book_name.setText(self.row[0].book_name)
            self.lineEdit_author.setText(self.row[0].author_name)
            if self.row[1]:
                self.lineEdit_translator.setText(self.row[1].author_name)
            self.lineEdit_press.setText(self.row[0].press_name)
            self.lineEdit_ISBN.setText(self.row[0].book_id)
            self.lineEdit_pressdate.setText(self.row[0].pressdate)
            self.lineEdit_version.setText(str(self.row[0].versions))
            self.lineEdit_price.setText(str(self.row[0].s_price))
            self.lineEdit_vip_price.setText(str(self.row[0].discount))
            self.lineEdit_stock.setText(str(self.row[0].reserve))
            self.intro.setPlainText(self.row[0].intro)
            index = self.comboBox_class1.findText(self.row[0].class1, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_class1.setCurrentIndex(index)
            self.get_class2(self.row[0].class1)
            if self.row[0].subclass:
                index = self.comboBox_class2.findText(self.row[0].subclass, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.comboBox_class2.setCurrentIndex(index)
            if self.row[0].graph:
                path = self.row[0].graph
                self.picture.setPixmap(QtGui.QPixmap(path))
            else:
                path = './icon/no_cover.jpg'
                self.picture.setPixmap(QtGui.QPixmap(path))

        # TODO:利用book_id调出图书信息，
        #      填到界面里，并且存到self.book_id里，intro还是intro，其它前面加个lineEdit比如lineEdit_book_name

            # 封面加入方法
            # path = './icon/test_pic2'
            # self.picture.setPixmap(QtGui.QPixmap(path))

    def save(self):
        """
        TODO:如果self.book_id不为None, 说明是双击表格进来的，把对书详细信息的改动保存到数据库
             如果self.book_id为None,说明是新增书目进来的，检验下除了简介封面译者以外的格子是不是都填了
             然后把新书的信息放到数据库，默认是未上架状态
        """
        option = [self.lineEdit_book_name.text(), self.lineEdit_author.text(), self.lineEdit_translator.text(),
                  self.lineEdit_press.text(), self.comboBox_class1.currentText(), self.comboBox_class2.currentText(),
                  self.lineEdit_class1.text(), self.lineEdit_class2.text(), self.lineEdit_ISBN.text(),
                  self.lineEdit_pressdate.text(), self.lineEdit_version.text(), self.lineEdit_price.text(),
                  self.lineEdit_vip_price.text(), self.intro.toPlainText(), self.lineEdit_stock.text()]
        if self.book_id:
            check = self.database.update_book(self.book_id, option)
        else:
            check = self.database.insert_book(option)
        if check == 0:
            QtWidgets.QMessageBox.about(self, '提示', '出版社不存在，请先在出版社管理界面填写相关出版社信息！')
        if check == 1:
            QtWidgets.QMessageBox.about(self, '提示', '未填写作者！')
        if check == 2:
            QtWidgets.QMessageBox.about(self, '提示', '未填写单价！')
        if check == 3:
            QtWidgets.QMessageBox.about(self, '提示', '未填写书名！')
        if check == 4:
            QtWidgets.QMessageBox.about(self, '提示', 'ISBN不允许为空也不允许修改！')
        if check == 5:
            QtWidgets.QMessageBox.about(self, '提示', '未填写出版日期！')
        if check == 6:
            QtWidgets.QMessageBox.about(self, '提示', '未填写版本号！')
        if check == 7:
            QtWidgets.QMessageBox.about(self, '提示', 'ISBN已存在！')
        if check == 8:
            QtWidgets.QMessageBox.about(self, '提示', 'ISBN已存在！')
        if check == -1:
            QtWidgets.QMessageBox.about(self, '提示', '保存成功！')
            self.switch_save.emit()

    def upload_cover(self):
        img = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', './', '图像文件 (*.jpg *.png)')[0]  # 选取文件 返回文件路径
        # TODO:把文件上传服务器和书对应起来
        self.picture.setPixmap(QtGui.QPixmap(img))  # 把图片放进画面里