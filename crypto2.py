import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog

from basic_algorithms_window import Ui_BasicAlgWindow
from main_window import Ui_mainWindow
from rsa_window import Ui_Form_RSA
from diffie_hellman_window import Ui_Form_DiffieHellman
from shamir_window import Ui_Form_Shamir
from elgamal_window import Ui_Form_ElGamal
from hash_window import Ui_Form_Hash
import basic_algorithms
import rsa
import diffie_hellman
import shamir
import elgamal
import md5


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
            self.window = DiffieHellmanWin()
        elif choice == "Криптосистема Шамира":
            self.window = ShamirWin()
        elif choice == "Криптосистема Эль-Гамаля":
            self.window = ElGamalWin()
        elif choice == "MD5":
            self.window = MD5HashWin()
        elif choice == "SHA":
            self.window = SHAHashWin()

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

class DiffieHellmanWin(QMainWindow, Ui_Form_DiffieHellman):
    def __init__(self, parent=None):
        super(DiffieHellmanWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_DiffieHellman()
        self.ui2.setupUi(self)
        self.ui2.action.triggered.connect(self.back)
        self.ui2.pushButton.clicked.connect(self.gener_a_g_p)
        self.ui2.pushButton_3.clicked.connect(self.calculated_A)
        self.ui2.pushButton_4.clicked.connect(self.gener_b)
        self.ui2.pushButton_2.clicked.connect(self.send_g_p_A)
        self.ui2.pushButton_5.clicked.connect(self.calculated_B)
        self.ui2.pushButton_6.clicked.connect(self.send_B)
        self.ui2.pushButton_7.clicked.connect(self.calculated_key_first)
        self.ui2.pushButton_8.clicked.connect(self.calculated_key_second)
        self.ui2.action_2.triggered.connect(self.change_len_num)


    def back(self):
        application.show()
        self.window().hide()

    def gener_a_g_p(self):
        msgShow("Возможна долгая генерация чисел. \nУменьшите длину чисел, если хотите ускорить генерацию.\nЗакройте это окно")
        len_num = int(self.ui2.lineEdit_13.text())
        a,g,p = diffie_hellman.generation_a_g_p(len_num)
        self.ui2.lineEdit.setText(str(a))
        self.ui2.lineEdit_2.setText(str(g))
        self.ui2.lineEdit_3.setText(str(p))
        msgShow("Рассчитайте A и отправьте клиенту Bob числа: g, p, A")

    def gener_b(self):
        len_num = int(self.ui2.lineEdit_13.text())
        b = diffie_hellman.generation_b(len_num)
        self.ui2.lineEdit_5.setText(str(b))
        msgShow("Получите от клиента Alice числа: g, p, A и рассчитайте число B")

    def calculated_A(self):
        len_num = int(self.ui2.lineEdit_13.text())
        a = self.ui2.lineEdit.text()
        g = self.ui2.lineEdit_2.text()
        p = self.ui2.lineEdit_3.text()

        if a.isdigit() and g.isdigit() and p.isdigit() and len(a) == len_num and len(g) == len_num and len(p) == len_num:
            self.ui2.lineEdit_4.setText(str(diffie_hellman.calculated(int(g),int(a),int(p))))
            msgShow("Получите от клиента Bob число B")
        else:
            msgShow("Введите или сгенерируйте числа")

    def send_g_p_A(self):
        len_num = int(self.ui2.lineEdit_13.text())
        g = self.ui2.lineEdit_2.text()
        p = self.ui2.lineEdit_3.text()
        A = self.ui2.lineEdit_4.text()
        if A.isdigit() and g.isdigit() and p.isdigit() and len(g) == len_num and len(p) == len_num:
            self.ui2.lineEdit_6.setText(g)
            self.ui2.lineEdit_7.setText(p)
            self.ui2.lineEdit_8.setText(A)

        else:
            msgShow("Введите или сгенерируйте числа, или рассчитайте A")

    def calculated_B(self):
        len_num = int(self.ui2.lineEdit_13.text())
        g = self.ui2.lineEdit_6.text()
        b = self.ui2.lineEdit_5.text()
        p = self.ui2.lineEdit_7.text()
        if g.isdigit() and b.isdigit() and p.isdigit() and len(g) == len_num and len(b) == len_num and len(p) == len_num:
            self.ui2.lineEdit_9.setText(str(diffie_hellman.calculated(int(g),int(b),int(p))))
            msgShow("Отправьте клиенту Alice число B и рассчитайте общий ключ")
        else:
            msgShow("Введите или получите числа")

    def send_B(self):
        len_num = int(self.ui2.lineEdit_13.text())
        B = self.ui2.lineEdit_9.text()
        if B.isdigit():
            self.ui2.lineEdit_10.setText(B)
        else:
            msgShow("Рассчитайте B")

    def calculated_key_first(self):
        len_num = int(self.ui2.lineEdit_13.text())
        B = self.ui2.lineEdit_10.text()
        a = self.ui2.lineEdit.text()
        p = self.ui2.lineEdit_3.text()
        if B.isdigit() and a.isdigit() and p.isdigit() and len(a) == len_num and len(p) == len_num:
            self.ui2.lineEdit_11.setText(str(diffie_hellman.calculated(int(B),int(a),int(p))))
        else:
            msgShow("Введите или получите числа")
        key_first = self.ui2.lineEdit_11.text()
        key_second = self.ui2.lineEdit_12.text()
        if key_first == key_second:
            msgShow("Общий ключ рассчитан \n"+ key_first)

    def calculated_key_second(self):
        len_num = int(self.ui2.lineEdit_13.text())
        A = self.ui2.lineEdit_8.text()
        b = self.ui2.lineEdit_5.text()
        p = self.ui2.lineEdit_7.text()
        if A.isdigit() and b.isdigit() and p.isdigit() and len(b) == len_num and len(p) == len_num:
            self.ui2.lineEdit_12.setText(str(diffie_hellman.calculated(int(A),int(b),int(p))))
        else:
            msgShow("Введите или получите числа")
        key_first = self.ui2.lineEdit_11.text()
        key_second = self.ui2.lineEdit_12.text()
        if key_first == key_second:
            msgShow("Общий ключ рассчитан: \n" + key_first)

    def change_len_num(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для чисел от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice)<= 200:
            self.ui2.lineEdit_13.setText(choice)
            self.ui2.label_15.setText("Длина чисел " + choice + " символов.")
        else:
            msgShow("Длина чисел задана неверно")
            return
        msgShow("Изменения успешно приняты")

class ShamirWin(QMainWindow,Ui_Form_Shamir):
    def __init__(self, parent=None):
        super(ShamirWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_Shamir()
        self.ui2.setupUi(self)
        self.ui2.action_2.triggered.connect(self.back)
        self.ui2.action.triggered.connect(self.change_len_keys)
        self.ui2.pushButton.clicked.connect(self.generated_p)
        self.ui2.pushButton_2.clicked.connect(self.send_message)

    def back(self):
        application.show()
        self.window().hide()

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice)<= 200:
            self.ui2.lineEdit_10.setText(choice)
            self.ui2.label_12.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина чисел задана неверно")
            return
        msgShow("Изменения успешно приняты")

    def generated_p(self):
        len_keys = int(self.ui2.lineEdit_10.text())
        self.ui2.lineEdit.setText(str(rsa.generation_prime_numb(len_keys)))
        self.ui2.textEdit_2.setText("")

    def send_message(self):
        len_keys = int(self.ui2.lineEdit_10.text())
        text = self.ui2.textEdit.toPlainText()
        if text == '':
            msgShow("Введите сообщение для передачи")
            return

        p = self.ui2.lineEdit.text()
        if p.isdigit() == False or len(p)!=len_keys:
            msgShow("Введите или сгенерируйте простое число")
            return
        text = shamir.text_to_blocks_num(text, len_keys)
        result = []
        for block in text:
            c_a, d_a = shamir.generation_c_and_d(int(p), len_keys)
            c_b, d_b = shamir.generation_c_and_d(int(p), len_keys)
            self.ui2.lineEdit_2.setText(str(c_a))
            self.ui2.lineEdit_3.setText(str(d_a))
            self.ui2.lineEdit_4.setText(str(c_b))
            self.ui2.lineEdit_5.setText(str(d_b))
            x1,x2,x3,x4 = shamir.send_block(int(block),c_a,d_a,c_b,d_b,int(p))
            self.ui2.lineEdit_6.setText(str(x1))
            self.ui2.lineEdit_7.setText(str(x2))
            self.ui2.lineEdit_8.setText(str(x3))
            self.ui2.lineEdit_9.setText(str(x4))
            result.append(str(x4))
            msgShow("Часть сообщения успешно передана")
            self.ui2.textEdit_2.insertPlainText(shamir.block_num_to_text(str(x4),len_keys))

class ElGamalWin(QMainWindow, Ui_Form_ElGamal):

    def __init__(self, parent=None):
        super(ElGamalWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_ElGamal()
        self.ui2.setupUi(self)
        self.ui2.action_5.triggered.connect(self.back)
        self.ui2.action_4.triggered.connect(self.change_len_keys)
        self.ui2.pushButton.clicked.connect(self.generation_p_g)
        self.ui2.pushButton_2.clicked.connect(self.send_message)
        self.ui2.action.triggered.connect(self.open_file_bytes)
        self.ui2.action_2.triggered.connect(self.open_file)
        self.ui2.action_3.triggered.connect(self.save_file)

    def back(self):
        application.show()
        self.window().hide()

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice)<= 200:
            self.ui2.lineEdit_11.setText(choice)
            self.ui2.label_13.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина чисел задана неверно")
            return
        msgShow("Изменения успешно приняты")

    def generation_p_g(self):
        len_keys = int(self.ui2.lineEdit_11.text())
        p,g = elgamal.generation_p_g(len_keys)
        self.ui2.lineEdit.setText(str(p))
        self.ui2.lineEdit_2.setText(str(g))
        self.ui2.textEdit_2.clear()
        return

    def send_message(self):
        len_keys = int(self.ui2.lineEdit_11.text())
        text = self.ui2.textEdit.toPlainText()
        if text == '':
            msgShow("Нет данных для отправки")
            return
        p = self.ui2.lineEdit.text()
        g = self.ui2.lineEdit_2.text()
        if p.isdigit() == False or len(p)!=len_keys or g.isdigit() == False \
                or basic_algorithms.modular_pow(int(g),int(p) - 1,int(p)) != 1:
            msgShow("Введите или сгенерируйте числа p и g")
            return
        blocks = shamir.text_to_blocks_num(text,len_keys)
        for block in blocks:
            c_a, d_a = elgamal.generation_c_d(len_keys,int(p),int(g))
            c_b, d_b = elgamal.generation_c_d(len_keys,int(p),int(g))
            self.ui2.lineEdit_3.setText(str(c_a))
            self.ui2.lineEdit_4.setText(str(d_a))
            self.ui2.lineEdit_8.setText(str(c_b))
            self.ui2.lineEdit_9.setText(str(d_b))
            k,r,e = elgamal.calculated_r_e(int(block),int(g),int(p),d_b)
            self.ui2.lineEdit_5.setText(str(k))
            self.ui2.lineEdit_6.setText(str(r))
            self.ui2.lineEdit_7.setText(str(e))
            m = elgamal.get_m(e,r,int(p),c_b)
            self.ui2.lineEdit_10.setText(str(m))
            block_text = shamir.block_num_to_text(block,len_keys)
            self.ui2.textEdit_2.insertPlainText(block_text)
            self.repaint()



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

        msgShow("Укажите расширение изначального файла.")

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
                    file.write(line + ' ')
            msgShow("Сохранение произошло успешно!")
            file.close()
        else:
            msgShow("Сохранение не произошло.")

class MD5HashWin(QMainWindow, Ui_Form_Hash):
    def __init__(self, parent=None):
        super(MD5HashWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_Hash()
        self.ui2.setupUi(self)
        self.setWindowTitle("MD5")
        self.ui2.action_4.triggered.connect(self.back)
        self.ui2.action.triggered.connect(self.open_file)
        self.ui2.action_2.triggered.connect(self.open_file_bytes)
        self.ui2.action_3.triggered.connect(self.save_in_file)
        self.ui2.pushButton.clicked.connect(self.hash_md5)

    def back(self):
        application.show()
        self.window().hide()

    def open_file(self):
        text = []
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'r') as file:
                for line in file:
                    text.append(line)
        except FileNotFoundError:

            return
        self.ui2.textEdit.setText(''.join(text))

    def open_file_bytes(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'rb') as file:
                text = file.read()
                self.ui2.lineEdit_2.setText("True")
                self.ui2.label_3.setText(fname)
        except FileNotFoundError:

            return
        self.ui2.textEdit.setText(str(text))

    def save_in_file(self):
        text = self.ui2.lineEdit.text()
        if text == '':
            msgShow("Нет данных для сохранения")
            return
        choice, ok = QInputDialog.getText(self, 'File names ', 'Укажите имя файла')
        if ok and choice != '':
            file = open(choice, 'w+')
            file.write(text)
            file.close()
            return

    def hash_md5(self):
        text = self.ui2.textEdit.toPlainText()
        fname = self.ui2.label_3.text()
        if text == '':
            msgShow("Нет данных для хэширования")
            return
        if fname == "":
            self.ui2.lineEdit.setText(md5.text_to_hash(text=text))
        else:
            self.ui2.lineEdit.setText(md5.text_to_hash(file_name=fname))
            self.ui2.label_3.setText("")


class SHAHashWin(QMainWindow, Ui_Form_Hash):
    def __init__(self, parent=None):
        super(SHAHashWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_Hash()
        self.ui2.setupUi(self)
        self.setWindowTitle("SHA")
        self.ui2.action_4.triggered.connect(self.back)


    def back(self):
        application.show()
        self.window().hide()



app = QApplication([])
application = MainWin()
application.show()


def msgShow(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()


sys.exit(app.exec())
