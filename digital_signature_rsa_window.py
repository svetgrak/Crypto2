# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digital_signature_rsa_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_DigSignRsa(object):
    def setupUi(self, Form_DigSignRsa):
        Form_DigSignRsa.setObjectName("Form_DigSignRsa")
        Form_DigSignRsa.resize(631, 429)
        Form_DigSignRsa.setMinimumSize(QtCore.QSize(631, 429))
        Form_DigSignRsa.setMaximumSize(QtCore.QSize(631, 429))
        self.centralwidget = QtWidgets.QWidget(Form_DigSignRsa)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 30, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 291, 51))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 181, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 171, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 281, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(2, 150, 54, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(2, 180, 54, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 281, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 141, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(2, 230, 54, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 230, 281, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(211, 90, 91, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 81, 17))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 300, 291, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 340, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 10, 54, 17))
        self.label_8.setObjectName("label_8")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 30, 301, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 110, 301, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 90, 81, 17))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 150, 181, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 190, 54, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 190, 281, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 220, 54, 17))
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(340, 220, 281, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 260, 221, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 330, 301, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(320, 310, 121, 17))
        self.label_12.setObjectName("label_12")
        Form_DigSignRsa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form_DigSignRsa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.action_3 = QtWidgets.QAction(Form_DigSignRsa)
        self.action_3.setObjectName("action_3")
        Form_DigSignRsa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form_DigSignRsa)
        self.statusbar.setObjectName("statusbar")
        Form_DigSignRsa.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Form_DigSignRsa)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Form_DigSignRsa)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(Form_DigSignRsa)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(Form_DigSignRsa)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.action_3)

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.label_13.hide()
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(450, 10, 200, 17))
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form_DigSignRsa)
        QtCore.QMetaObject.connectSlotsByName(Form_DigSignRsa)

    def retranslateUi(self, Form_DigSignRsa):
        _translate = QtCore.QCoreApplication.translate
        Form_DigSignRsa.setWindowTitle(_translate("Form_DigSignRsa", "Form_DigSignRsa"))
        self.label.setText(_translate("Form_DigSignRsa", "Данные:"))
        self.pushButton.setText(_translate("Form_DigSignRsa", "Сгенерировать подпись"))
        self.label_2.setText(_translate("Form_DigSignRsa", "Открытые ключи: "))
        self.label_3.setText(_translate("Form_DigSignRsa", "N:"))
        self.label_4.setText(_translate("Form_DigSignRsa", "d:"))
        self.label_5.setText(_translate("Form_DigSignRsa", "Закрытый ключ:"))
        self.label_6.setText(_translate("Form_DigSignRsa", "c:"))
        self.comboBox.setItemText(0, _translate("Form_DigSignRsa", "md5"))
        self.comboBox.setItemText(1, _translate("Form_DigSignRsa", "sha1"))
        self.label_7.setText(_translate("Form_DigSignRsa", "Подпись:"))
        self.pushButton_2.setText(_translate("Form_DigSignRsa", "Отправить сообщение с подписью"))
        self.label_8.setText(_translate("Form_DigSignRsa", "Данные:"))
        self.label_9.setText(_translate("Form_DigSignRsa", "Подпись:"))
        self.pushButton_3.setText(_translate("Form_DigSignRsa", "Получить ключи"))
        self.label_10.setText(_translate("Form_DigSignRsa", "N:"))
        self.label_11.setText(_translate("Form_DigSignRsa", "d:"))
        self.pushButton_4.setText(_translate("Form_DigSignRsa", "Проверить подпись"))
        self.label_12.setText(_translate("Form_DigSignRsa", "Результат:"))
        self.menu.setTitle(_translate("Form_DigSignRsa", "Файл"))
        self.menu_2.setTitle(_translate("Form_DigSignRsa", "Ключи"))
        self.action_3.setText(_translate("Form_DigSignRsa", "Назад"))
        self.action.setText(_translate("Form_DigSignRsa", "Загрузить файл"))
        self.action_2.setText(_translate("Form_DigSignRsa", "Задать длину ключей"))
        self.action_4.setText(_translate("Form_DigSignRsa", "Загрузить подпись и ключи"))
        self.action_5.setText(_translate("Form_DigSignRsa", "Сохранить подпись и ключи"))
        self.label_13.setText(_translate("Form_DigSignRsa", "50"))
        self.label_15.setText(_translate("Form_DigSignRsa", "Длина ключей 50 символов."))
