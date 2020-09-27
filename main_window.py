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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 60, 121, 30))
        self.pushButton.setObjectName("pushButton")






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
        self.comboBox.setItemText(0, _translate("mainWindow", " "))
        self.comboBox.setItemText(1, _translate("mainWindow", "Базовые алгоритмы теории чиел"))
        self.comboBox.setItemText(2, _translate("mainWindow", "RSA"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Метод ключевого обмена Диффи-Хелмана"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Криптосистема Шамира"))
        self.comboBox.setItemText(5, _translate("mainWindow", "Криптосистема Эль-Гамаля"))

        self.pushButton.setText(_translate("mainWindow", "Далее"))


        

        self.label_4.setText(_translate("mainWindow", "Created by svetgrak "))

