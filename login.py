# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QMessageBox, QApplication, QDialog
import user
import registerwindow
import Stu_AppWindow
import TeacWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 562)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setStyleSheet("font: 9pt \"新宋体\";\n"
"font: 24pt \"华光行草_CNKI\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.id_text = QtWidgets.QLineEdit(self.centralwidget)
        self.id_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_text.setObjectName("id_text")
        self.verticalLayout.addWidget(self.id_text)
        self.name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.name_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_text.setObjectName("name_text")
        self.verticalLayout.addWidget(self.name_text)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
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
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.register_2.setObjectName("register_2")
        self.horizontalLayout.addWidget(self.register_2)
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setStyleSheet("border-color: rgb(172, 172, 172);\n"
"background-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 注册功能的信号与槽连接
        self.register_2.clicked.connect(self.openreg)
        self.login.clicked.connect(self.openApplication)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进出校管理系统"))
        self.title.setText(_translate("MainWindow", "进出校管理系统"))
        self.id_text.setPlaceholderText(_translate("MainWindow", "请输入学号或工号"))
        self.name_text.setPlaceholderText(_translate("MainWindow", "请输入姓名"))
        self.comboBox.setItemText(0, _translate("MainWindow", "材料学院"))
        self.comboBox.setItemText(1, _translate("MainWindow", "法学院"))
        self.comboBox.setItemText(2, _translate("MainWindow", "高等研究院"))
        self.comboBox.setItemText(3, _translate("MainWindow", "五道口金融书院"))
        self.comboBox.setItemText(4, _translate("MainWindow", "工程物理系"))
        self.comboBox.setItemText(5, _translate("MainWindow", "公管学院"))
        self.comboBox.setItemText(6, _translate("MainWindow", "航空航天学院"))
        self.comboBox.setItemText(7, _translate("MainWindow", "化学工程系"))
        self.comboBox.setItemText(8, _translate("MainWindow", "环境学院"))
        self.comboBox.setItemText(9, _translate("MainWindow", "机械工程系"))
        self.comboBox.setItemText(10, _translate("MainWindow", "精密仪器系"))
        self.comboBox.setItemText(11, _translate("MainWindow", "能源与动力系"))
        self.comboBox.setItemText(12, _translate("MainWindow", "车辆与运载学院"))
        self.comboBox.setItemText(13, _translate("MainWindow", "工业工程系"))
        self.comboBox.setItemText(14, _translate("MainWindow", "建筑学院"))
        self.comboBox.setItemText(15, _translate("MainWindow", "经济管理学院"))
        self.comboBox.setItemText(16, _translate("MainWindow", "数学系"))
        self.comboBox.setItemText(17, _translate("MainWindow", "物理系"))
        self.comboBox.setItemText(18, _translate("MainWindow", "化学系"))
        self.comboBox.setItemText(19, _translate("MainWindow", "地球系统科学系"))
        self.comboBox.setItemText(20, _translate("MainWindow", "天文系"))
        self.comboBox.setItemText(21, _translate("MainWindow", "马克思主义学院"))
        self.comboBox.setItemText(22, _translate("MainWindow", "美术学院"))
        self.comboBox.setItemText(23, _translate("MainWindow", "人文学院"))
        self.comboBox.setItemText(24, _translate("MainWindow", "求真书院"))
        self.comboBox.setItemText(25, _translate("MainWindow", "社会科学学院"))
        self.comboBox.setItemText(26, _translate("MainWindow", "日新书院"))
        self.comboBox.setItemText(27, _translate("MainWindow", "探微书院"))
        self.comboBox.setItemText(28, _translate("MainWindow", "未央书院"))
        self.comboBox.setItemText(29, _translate("MainWindow", "致理书院"))
        self.comboBox.setItemText(30, _translate("MainWindow", "行健书院"))
        self.comboBox.setItemText(31, _translate("MainWindow", "药学院"))
        self.comboBox.setItemText(32, _translate("MainWindow", "医学院"))
        self.comboBox.setItemText(33, _translate("MainWindow", "新雅书院"))
        self.comboBox.setItemText(34, _translate("MainWindow", "新闻与传播学院"))
        self.comboBox.setItemText(35, _translate("MainWindow", "苏世民书院"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "学生"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "教师"))
        self.register_2.setText(_translate("MainWindow", "注册"))
        self.login.setText(_translate("MainWindow", "登录"))

    # 注册界面打开
    def openreg(self):
        self.form = QWidget()
        self.ui = registerwindow.Ui_widget()
        self.ui.setupUi(self.form)
        self.form.show()

    # 申请界面打开
    def openApplication(self):
        exist_warning = QWidget()
        empty_warning = QWidget()
        logins = user.regipro()
        id = self.id_text.text()
        name = self.name_text.text()
        dep_id = self.comboBox.currentIndex() + 1
        stu_teac = self.comboBox_2.currentIndex() + 1
        if (stu_teac == 1):
            stu_teac = 'student'
        else:
            stu_teac = 'teacher'
        if ((len(id) == 0) | (len(name) == 0)):
            QMessageBox.information(empty_warning, "提示", "输入不能为空")
        else:
            IfExist = logins.CheckStu_Tea(int(id), name, dep_id, stu_teac)
            if ((stu_teac == 'student') & (IfExist == 1)):
                self.formstu = QWidget()
                self.stu_ui = Stu_AppWindow.Ui_Form(name, id)
                self.stu_ui.setupUi(self.formstu)
                self.formstu.show()
                self.MainWindow.hide()
            elif((stu_teac == 'student') & (IfExist == 0)):
                QMessageBox.information(exist_warning, "提示", "没有此学生")
            elif((stu_teac == 'teacher') & (IfExist == 1)):
                self.formteac = QWidget()
                self.teac_ui = TeacWindow.Ui_Teac(name, id)
                self.teac_ui.setupUi(self.formteac)
                self.formteac.show()
                self.MainWindow.hide()
            elif((stu_teac == 'teacher') & (IfExist == 0)):
                QMessageBox.information(exist_warning, "提示", "没有此教师")