# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget,QMessageBox,QApplication
import user


class Ui_widget(object):
    def setupUi(self, widget):
        self.reg_type = ''
        widget.setObjectName("widget")
        widget.resize(1000, 500)
        widget.setMinimumSize(QtCore.QSize(100, 100))
        widget.setMaximumSize(QtCore.QSize(700, 700))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(widget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.id = QtWidgets.QLineEdit(widget)
        self.id.setObjectName("id")
        self.verticalLayout.addWidget(self.id)
        self.phonenum = QtWidgets.QLineEdit(widget)
        self.phonenum.setObjectName("phonenum")
        self.verticalLayout.addWidget(self.phonenum)
        self.email = QtWidgets.QLineEdit(widget)
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.comboBox = QtWidgets.QComboBox(widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_student = QtWidgets.QPushButton(widget)
        self.check_student.setObjectName("check_student")
        self.horizontalLayout_2.addWidget(self.check_student)
        self.checkteacher = QtWidgets.QPushButton(widget)
        self.checkteacher.setObjectName("checkteacher")
        self.horizontalLayout_2.addWidget(self.checkteacher)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_reg = QtWidgets.QPushButton(widget)
        self.btn_reg.setObjectName("btn_reg")
        self.verticalLayout.addWidget(self.btn_reg)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        # 信号与槽连接
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)
        self.check_student.clicked.connect(self.on_checkstudent_clicked)
        self.checkteacher.clicked.connect(self.on_checkteacher_clicked)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "注册"))
        self.name.setPlaceholderText(_translate("widget", "请输入姓名"))
        self.id.setPlaceholderText(_translate("widget", "请输入正确学号或工号"))
        self.phonenum.setPlaceholderText(_translate("widget", "请输入电话号码"))
        self.email.setPlaceholderText(_translate("widget", "请输入邮箱地址"))
        self.comboBox.setItemText(0, _translate("widget", "材料学院"))
        self.comboBox.setItemText(1, _translate("widget", "法学院"))
        self.comboBox.setItemText(2, _translate("widget", "高等研究院"))
        self.comboBox.setItemText(3, _translate("widget", "五道口金融书院"))
        self.comboBox.setItemText(4, _translate("widget", "工程物理系"))
        self.comboBox.setItemText(5, _translate("widget", "公管学院"))
        self.comboBox.setItemText(6, _translate("widget", "航空航天学院"))
        self.comboBox.setItemText(7, _translate("widget", "化学工程系"))
        self.comboBox.setItemText(8, _translate("widget", "环境学院"))
        self.comboBox.setItemText(9, _translate("widget", "机械工程系"))
        self.comboBox.setItemText(10, _translate("widget", "精密仪器系"))
        self.comboBox.setItemText(11, _translate("widget", "能源与动力系"))
        self.comboBox.setItemText(12, _translate("widget", "车辆与运载学院"))
        self.comboBox.setItemText(13, _translate("widget", "工业工程系"))
        self.comboBox.setItemText(14, _translate("widget", "建筑学院"))
        self.comboBox.setItemText(15, _translate("widget", "经济管理学院"))
        self.comboBox.setItemText(16, _translate("widget", "数学系"))
        self.comboBox.setItemText(17, _translate("widget", "物理系"))
        self.comboBox.setItemText(18, _translate("widget", "化学系"))
        self.comboBox.setItemText(19, _translate("widget", "地球系统科学系"))
        self.comboBox.setItemText(20, _translate("widget", "天文系"))
        self.comboBox.setItemText(21, _translate("widget", "马克思主义学院"))
        self.comboBox.setItemText(22, _translate("widget", "美术学院"))
        self.comboBox.setItemText(23, _translate("widget", "人文学院"))
        self.comboBox.setItemText(24, _translate("widget", "求真书院"))
        self.comboBox.setItemText(25, _translate("widget", "社会科学学院"))
        self.comboBox.setItemText(26, _translate("widget", "日新书院"))
        self.comboBox.setItemText(27, _translate("widget", "探微书院"))
        self.comboBox.setItemText(28, _translate("widget", "未央书院"))
        self.comboBox.setItemText(29, _translate("widget", "致理书院"))
        self.comboBox.setItemText(30, _translate("widget", "行健书院"))
        self.comboBox.setItemText(31, _translate("widget", "药学院"))
        self.comboBox.setItemText(32, _translate("widget", "医学院"))
        self.comboBox.setItemText(33, _translate("widget", "新雅书院"))
        self.comboBox.setItemText(34, _translate("widget", "新闻与传播学院"))
        self.comboBox.setItemText(35, _translate("widget", "苏世民书院"))
        self.check_student.setText(_translate("widget", "学生"))
        self.checkteacher.setText(_translate("widget", "教师"))
        self.btn_reg.setText(_translate("widget", "注册"))

    def on_checkteacher_clicked(self):
        self.reg_type = 'teacher'
        self.check_student.setEnabled(False)

    def on_checkstudent_clicked(self):
        self.reg_type = 'student'
        self.checkteacher.setEnabled(False)

    # 注
    def on_btn_reg_clicked(self):
        regis = user.regipro()
        empty_warning = QWidget()
        success_information = QWidget()
        repetition = QWidget()
        id_text = self.id.text()
        name_text = self.name.text()
        phonenum_text = self.phonenum.text()
        email_text = self.email.text()
        dep_id = self.comboBox.currentIndex() + 1
        if ((len(id_text) == 0) | (len(name_text) == 0) | (len(phonenum_text) == 0) | (len(email_text)) == 0 | (
                self.reg_type.strip() == '')):
            QMessageBox.information(empty_warning, "警告", "输入内容不能为空")
        else:
            IfExist = regis.Adduser(int(id_text), name_text, int(phonenum_text), email_text, dep_id, self.reg_type)
            if (IfExist == 0):
                # 检查是否已经有一样的id存在
                QMessageBox.information(repetition, "警告", "此ID已存在")
            else:
                # 成功就将按钮置灰
                self.btn_reg.setEnabled(False)
                QMessageBox.information(success_information, "提示", "注册成功")