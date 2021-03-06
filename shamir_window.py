from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Shamir(object):
    def setupUi(self, Form_Shamir):
        Form_Shamir.setObjectName("Form_Shamir")
        Form_Shamir.resize(563, 450)
        Form_Shamir.setMinimumSize(QtCore.QSize(563, 450))
        Form_Shamir.setMaximumSize(QtCore.QSize(563, 450))
        self.centralwidget = QtWidgets.QWidget(Form_Shamir)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 17))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 541, 70))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 171, 17))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 330, 541, 70))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 511, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 54, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 140, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 170, 221, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 200, 221, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 170, 231, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 200, 231, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 54, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 54, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 170, 54, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 200, 54, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 240, 54, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 240, 54, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 270, 54, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(300, 270, 54, 17))
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 240, 221, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(320, 240, 231, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(40, 270, 221, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(320, 270, 231, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 140, 141, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        Form_Shamir.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form_Shamir)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Form_Shamir.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form_Shamir)
        self.statusbar.setObjectName("statusbar")
        Form_Shamir.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Form_Shamir)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.action_2 = QtWidgets.QAction(self.menubar)
        self.action_2.setObjectName("action_2")
        self.menubar.addAction(self.action_2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.hide()
        self.lineEdit_10.setText("50")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QtCore.QRect(380, 10, 171, 17))


        self.retranslateUi(Form_Shamir)
        QtCore.QMetaObject.connectSlotsByName(Form_Shamir)

    def retranslateUi(self, Form_Shamir):
        _translate = QtCore.QCoreApplication.translate
        Form_Shamir.setWindowTitle(_translate("Form_Shamir", "Shamir"))
        self.label.setText(_translate("Form_Shamir", "Сообщение: "))
        self.label_2.setText(_translate("Form_Shamir", "Полученное сообщение:"))
        self.label_3.setText(_translate("Form_Shamir", "p:"))
        self.pushButton.setText(_translate("Form_Shamir", "Сгенерировать p"))
        self.label_4.setText(_translate("Form_Shamir", "c(a):"))
        self.label_5.setText(_translate("Form_Shamir", "d(a):"))
        self.label_6.setText(_translate("Form_Shamir", "c(b):"))
        self.label_7.setText(_translate("Form_Shamir", "d(b):"))
        self.label_8.setText(_translate("Form_Shamir", "x1:"))
        self.label_9.setText(_translate("Form_Shamir", "x2:"))
        self.label_10.setText(_translate("Form_Shamir", "x3:"))
        self.label_11.setText(_translate("Form_Shamir", "x4:"))
        self.pushButton_2.setText(_translate("Form_Shamir", "Отправить сообщение"))
        self.menu.setTitle(_translate("Form_Shamir", "Ключи"))
        self.action.setText(_translate("Form_Shamir", "Задать длину ключей"))
        self.action_2.setText(_translate("Form_Shamir", "Назад"))
        self.label_12.setText(_translate("Form_Shamir", "Длина ключей 50 символов."))
