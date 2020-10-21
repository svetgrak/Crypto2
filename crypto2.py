import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog
from basic_algorithms_window import Ui_BasicAlgWindow
from main_window import Ui_mainWindow
from rsa_window import Ui_Form_RSA
import basic_algorithms
import rsa


class MainWin(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_next_win)

    def open_next_win(self):
        choice = str(self.ui.comboBox.currentText())
        if choice == "":
            msgShow("Выберите алгоритм из списка")
        elif choice == "Базовые алгоритмы теории чисел":
            self.window = BasicAlgWin()
        elif choice == "RSA":
            self.window = RSAWin()
        elif choice == "Метод ключевого обмена Диффи-Хелмана":
            msgShow('2')
        self.window.show()
        application.hide()


class BasicAlgWin(QMainWindow, Ui_BasicAlgWindow):

    def __init__(self, parent=None):
        super(BasicAlgWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_BasicAlgWindow()
        self.ui2.setupUi(self)
        self.ui2.pushButton.clicked.connect(self.pow)
        self.ui2.pushButton_2.clicked.connect(self.gcd)
        self.ui2.pushButton_3.clicked.connect(self.invert)
        self.ui2.action.triggered.connect(self.back)
        self.ui2.action.setStatusTip("Вернуться к выбору алгоритма")

    def pow(self):
        a = self.ui2.lineEdit.text()
        x = self.ui2.lineEdit_2.text()
        p = self.ui2.lineEdit_3.text()

        if a.isdigit() and x.isdigit() and p.isdigit():
            self.ui2.lineEdit_4.setText(str(basic_algorithms.modular_pow(int(a), int(x), int(p))))
        else:
            msgShow("Введите целые числа")

    def gcd(self):
        a = self.ui2.lineEdit_5.text()
        b = self.ui2.lineEdit_6.text()
        if a.isdigit() and b.isdigit():
            self.ui2.lineEdit_7.setText(str(basic_algorithms.gcd(int(a), int(b))))
        else:
            msgShow("Введите целые числа")

    def invert(self):
        x = self.ui2.lineEdit_8.text()
        p = self.ui2.lineEdit_9.text()
        if x.isdigit() and p.isdigit():
            self.ui2.lineEdit_10.setText(str(basic_algorithms.invert(int(x), int(p))))
        else:
            msgShow("Введите целые числа")

    def back(self):
        application.show()
        self.window().hide()

class RSAWin(QMainWindow, Ui_Form_RSA):

    def __init__(self, parent=None):
        super(RSAWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_RSA()
        self.ui2.setupUi(self)
        self.ui2.action_6.triggered.connect(self.back)
        self.ui2.action_6.setStatusTip("Вернуться к выбору алгоритма")
        self.ui2.action.triggered.connect(self.open_file_bytes)
        self.ui2.action.setStatusTip("Загрузить файл для шифрования")
        self.ui2.action_2.triggered.connect(self.open_file)
        self.ui2.action_2.setStatusTip("Загрузить данные из файла")
        self.ui2.action_7.triggered.connect(self.save_file)
        self.ui2.action_7.setStatusTip("Сохранить результат")
        self.ui2.action_3.triggered.connect(self.download_keys)
        self.ui2.action_3.setStatusTip("Загрузить ключи из файлов (закрытый ключ хранится в отдельном)")
        self.ui2.action_4.triggered.connect(self.save_keys)
        self.ui2.action_4.setStatusTip("Сохранить ключи в файлы (закрытый ключ сохраните в отдельный файл)")
        self.ui2.action_5.triggered.connect(self.change_len_keys)
        self.ui2.action_5.setStatusTip("Установить свою длину генерируемых ключей (от 20 знаков до 200)")
        self.ui2.pushButton.clicked.connect(self.generation_keys)
        self.ui2.pushButton_2.clicked.connect(self.encrypt)
        self.ui2.pushButton_3.clicked.connect(self.decrypt)

    def back(self):
        application.show()
        self.window().hide()

    def generation_keys(self):
        len_keys = int(self.ui2.lineEdit_4.text())
        e, n, d = rsa.generation_keys(len_keys)
        self.ui2.lineEdit.setText(str(e))
        self.ui2.lineEdit_2.setText(str(n))
        self.ui2.lineEdit_3.setText(str(d))

    def encrypt(self):
        text = self.ui2.textEdit.toPlainText()
        len_keys = int(self.ui2.lineEdit_4.text())

        e = self.ui2.lineEdit.text()
        n = self.ui2.lineEdit_2.text()
        if e.isdigit() and n.isdigit() and len(n) == len_keys:
            if text != "":
                self.ui2.textEdit_2.setText(rsa.encrypt(text, int(e), int(n)))
            else:
                msgShow("Введите или загрузите данные")
        else:
            msgShow(str(len_keys))
            msgShow("Введите, сгенерируйте или загрузите ключи. \n"
                    "Проверьте, чтобы длина ключей совпадала с установленной")

    def decrypt(self):
        text = self.ui2.textEdit.toPlainText()
        len_keys = int(self.ui2.lineEdit_4.text())
        d = self.ui2.lineEdit_3.text()
        n = self.ui2.lineEdit_2.text()
        if d.isdigit() and n.isdigit() and len(d) == len_keys and len(n) == len_keys:
            if text != "":
                self.ui2.textEdit_2.setText(rsa.decrypt(text, int(d), int(n)))
            else:
                msgShow("Введите или загрузите данные")
        else:
            msgShow("Введите, сгенерируйте или загрузите ключи. \n"
                    "Проверьте, чтобы длина ключей совпадала с установленной")

    def open_file_bytes(self):
        bytelist = []
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'rb') as file:
                for byte in file:
                    for ch in byte:
                        bytelist.append(str(ch))
        except FileNotFoundError:
            msgShow("Выберите существующий файл")
            return
        self.ui2.textEdit.setText(' '.join(bytelist))

    def open_file(self):
        text = []
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'r') as file:
                for line in file:
                    text.append(line)
        except FileNotFoundError:
            msgShow("Выберите существующий файл")
            return
        self.ui2.textEdit.setText(''.join(text))

    def save_file(self):
        text_bytes = self.ui2.textEdit_2.toPlainText()
        if text_bytes == "":
            msgShow("Нет данных для сохранения")
            return

        msgShow("Если вы шифровали файл, то вместе с зашифрованной информацией \n"
                "передайте исходное расширание файла.\n"
                "Если вы расшифровываете файл, укажите расширение изначального файла.")

        choice, ok = QInputDialog.getText(self, 'File name ', 'input File name')
        if ok and choice != '':
            text_bytes = text_bytes.split()
            if text_bytes[0].isdigit() and int(text_bytes[0]) < 256:
                text_bytes = rsa.text_to_byte(text_bytes)
                file = open(choice, 'wb+')
                for ch in text_bytes:
                    file.write(ch)
            else:
                file = open(choice, 'w+')
                for line in text_bytes:
                    file.write(line+' ')
            msgShow("Сохранение произошло успешно!")
            file.close()
        else:
            msgShow("Сохранение не произошло.")

    def download_keys(self):
        choice, ok = QInputDialog.getText(self, 'File names ', 'Укажите имена файлов для открытых \n и закрытого ключей через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 2:
                msgShow("Введите 2 файла")
                return
            try:
                file = open(choice[0], 'r')
                e = file.readline()[:-2]
                n = file.readline()
                file.close()
                if e.isdigit() == False and n.isdigit() == False:
                    msgShow("Ключи не удовлетворяют формату")
                    return
                self.ui2.lineEdit_4.setText(str(len(n)))
                self.ui2.label_8.setText("Длина ключей "+ str(len(n))+ " символов.")
                self.ui2.lineEdit.setText(e)
                self.ui2.lineEdit_2.setText(n)
                file = open(choice[1], 'r')
                d = file.read()
                file.close()
            except FileNotFoundError:
                msgShow("Выберите существующие файлы")
                return
            if d.isdigit() == False:
                msgShow("Ключи не удовлетворяют формату")
                return
            if len(d) != len(n):
                msgShow("Длина закрытого и открытого ключей различна")
                return
            self.ui2.lineEdit_3.setText(d)

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice)<= 200:
            self.ui2.lineEdit_4.setText(choice)
            self.ui2.label_8.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина ключей задана неверно")
        msgShow("Изменения успешно приняты")

    def save_keys(self):
        len_keys = self.ui2.lineEdit_4.text()
        e = self.ui2.lineEdit.text()
        n = self.ui2.lineEdit_2.text()
        d = self.ui2.lineEdit_3.text()
        if e == '' and e.isdigit() == False and n == '' and n.isdigit() == False and len(n) != int(
                len_keys) and d == '' and d.isdigit() == False and len(d) != int(len_keys):
            msgShow("Ключи не удовлетворяют формату")
            return
        choice, ok = QInputDialog.getText(self, 'File names ', 'Укажите имена файлов для открытых \n и закрытого ключей через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice)!= 2:
                msgShow("Введите 2 файла")
                return
            try:
                file = open(choice[0], 'w+')
                file.write(e + '\n'+n)
                file.close()
                file = open(choice[1], 'w+')
                file.write(d)
                file.close()
            except FileNotFoundError:
                msgShow("Укажите верные файлы")
                return
            msgShow("Ключи успешно сохранены")
        else:
            msgShow("Сохранение не произошло")



app = QApplication([])
application = MainWin()
application.show()


def msgShow(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()


sys.exit(app.exec())
