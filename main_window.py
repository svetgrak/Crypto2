from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")

        mainWindow.resize(600, 400)
        mainWindow.setMaximumSize(QtCore.QSize(600, 400))
        mainWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 350, 17))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 350, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 350, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 150, 350, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 350, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 240, 350, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 60, 121, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 150, 121, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 121, 30))
        self.pushButton_3.setObjectName("pushButton_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 350, 350, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: rgb(176, 176, 176) ")
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(15)
        self.label_4.setFont(font)


        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Crypto2"))
        self.label.setText(_translate("mainWindow", "Ассиметричные криптосистемы :"))
        self.comboBox.setItemText(0, _translate("mainWindow", ""))
        self.comboBox.setItemText(1, _translate("mainWindow", "Базовые алгоритмы теории чисел"))
        self.comboBox.setItemText(2, _translate("mainWindow", "RSA"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Метод ключевого обмена Диффи-Хелмана"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Криптосистема Шамира"))
        self.comboBox.setItemText(5, _translate("mainWindow", "Криптосистема Эль-Гамаля"))

        self.label_2.setText(_translate("mainWindow", "Алгоритмы хэширования :"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", ""))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "MD5"))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "SHA-1"))
        self.label_3.setText(_translate("mainWindow", "Электронная подпись :"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", ""))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "на базе RSA"))
        self.comboBox_3.setItemText(2, _translate("mainWindow", "на базе Эль-Гамаля"))


        self.pushButton.setText(_translate("mainWindow", "Далее"))
        self.pushButton_2.setText(_translate("mainWindow", "Далее"))
        self.pushButton_3.setText(_translate("mainWindow", "Далее"))

        self.label_4.setText(_translate("mainWindow", "Created by svetgrak "))

