import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog
from basic_algorithms_window import Ui_BasicAlgWindow
from main_window import Ui_mainWindow
from rsa_window import Ui_Form_RSA
from diffie_hellman_window import Ui_Form_DiffieHellman
from shamir_window import Ui_Form_Shamir
from elgamal_window import Ui_Form_ElGamal
from hash_window import Ui_Form_Hash
from digital_signature_rsa_window import Ui_Form_DigSignRsa
from digital_signature_elgamal_window import Ui_Form_DigSignElGamal
from dsa_window import Ui_Form_DSA
import basic_algorithms
import rsa
import diffie_hellman
import shamir
import elgamal
import md5
import sha1
import digital_signature_rsa
import digital_signature_elgamal
import dsa


class MainWin(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_next_win_1)
        self.ui.pushButton_2.clicked.connect(self.open_next_win_2)
        self.ui.pushButton_3.clicked.connect(self.open_next_win_3)

    def open_next_win_1(self):

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
        try:
            self.window.show()
            application.hide()
        except AttributeError:
            return

    def open_next_win_2(self):
        choice = str(self.ui.comboBox_2.currentText())
        if choice == "":
            msgShow("Выберите алгоритм из списка")
        elif choice == "MD5":
            self.window = MD5HashWin()
        elif choice == "SHA-1":
            self.window = SHAHashWin()
        try:
            self.window.show()
            application.hide()
        except AttributeError:
            return

    def open_next_win_3(self):
        choice = str(self.ui.comboBox_3.currentText())
        if choice == "":
            msgShow("Выберите алгоритм из списка")
        elif choice == "на базе RSA":
            self.window = DigSignRSAWin()
        elif choice == "на базе Эль-Гамаля":
            self.window = DigSignElGamalWin()
        elif choice == "DSA":
            self.window = DSAWin()
        try:
            self.window.show()
            application.hide()
        except AttributeError:
            return


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
                    file.write(line + ' ')
            msgShow("Сохранение произошло успешно!")
            file.close()
        else:
            msgShow("Сохранение не произошло.")

    def download_keys(self):
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых \n и закрытого ключей через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 2:
                msgShow("Введите 2 файла")
                return
            try:
                file = open(choice[0], 'r')
                e = file.readline()[:-1]
                n = file.readline()
                file.close()
                if e.isdigit() == False and n.isdigit() == False:
                    msgShow("Ключи не удовлетворяют формату")
                    return
                self.ui2.lineEdit_4.setText(str(len(n)))
                self.ui2.label_8.setText("Длина ключей " + str(len(n)) + " символов.")
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
        if choice.isdigit() and int(choice) >= 20 and int(choice) <= 200:
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
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых \n и закрытого ключей через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 2:
                msgShow("Введите 2 файла")
                return
            try:
                file = open(choice[0], 'w+')
                file.write(e + '\n' + n)
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
        self.ui2.action.setStatusTip("Вернуться к выбору алгоритма")
        self.ui2.action_2.setStatusTip("Установить свою длину генерируемых ключей (от 20 знаков до 200)")

    def back(self):
        application.show()
        self.window().hide()

    def gener_a_g_p(self):
        msgShow(
            "Возможна долгая генерация чисел. \nУменьшите длину чисел, если хотите ускорить генерацию.\nЗакройте это окно")
        len_num = int(self.ui2.lineEdit_13.text())
        a, g, p = diffie_hellman.generation_a_g_p(len_num)
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

        if a.isdigit() and g.isdigit() and p.isdigit() and len(a) == len_num and len(g) == len_num and len(
                p) == len_num:
            self.ui2.lineEdit_4.setText(str(diffie_hellman.calculated(int(g), int(a), int(p))))
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
        if g.isdigit() and b.isdigit() and p.isdigit() and len(g) == len_num and len(b) == len_num and len(
                p) == len_num:
            self.ui2.lineEdit_9.setText(str(diffie_hellman.calculated(int(g), int(b), int(p))))
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
            self.ui2.lineEdit_11.setText(str(diffie_hellman.calculated(int(B), int(a), int(p))))
        else:
            msgShow("Введите или получите числа")
        key_first = self.ui2.lineEdit_11.text()
        key_second = self.ui2.lineEdit_12.text()
        if key_first == key_second:
            msgShow("Общий ключ рассчитан \n" + key_first)

    def calculated_key_second(self):
        len_num = int(self.ui2.lineEdit_13.text())
        A = self.ui2.lineEdit_8.text()
        b = self.ui2.lineEdit_5.text()
        p = self.ui2.lineEdit_7.text()
        if A.isdigit() and b.isdigit() and p.isdigit() and len(b) == len_num and len(p) == len_num:
            self.ui2.lineEdit_12.setText(str(diffie_hellman.calculated(int(A), int(b), int(p))))
        else:
            msgShow("Введите или получите числа")
        key_first = self.ui2.lineEdit_11.text()
        key_second = self.ui2.lineEdit_12.text()
        if key_first == key_second:
            msgShow("Общий ключ рассчитан: \n" + key_first)

    def change_len_num(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для чисел от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice) <= 200:
            self.ui2.lineEdit_13.setText(choice)
            self.ui2.label_15.setText("Длина чисел " + choice + " символов.")
        else:
            msgShow("Длина чисел задана неверно")
            return
        msgShow("Изменения успешно приняты")


class ShamirWin(QMainWindow, Ui_Form_Shamir):
    def __init__(self, parent=None):
        super(ShamirWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_Shamir()
        self.ui2.setupUi(self)
        self.ui2.action_2.triggered.connect(self.back)
        self.ui2.action.triggered.connect(self.change_len_keys)
        self.ui2.pushButton.clicked.connect(self.generated_p)
        self.ui2.pushButton_2.clicked.connect(self.send_message)
        self.ui2.action_2.setStatusTip("Вернуться к выбору алгоритма")
        self.ui2.action.setStatusTip("Установить свою длину генерируемых ключей (от 20 знаков до 200)")

    def back(self):
        application.show()
        self.window().hide()

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice) <= 200:
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
        if p.isdigit() == False or len(p) != len_keys:
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
            x1, x2, x3, x4 = shamir.send_block(int(block), c_a, d_a, c_b, d_b, int(p))
            self.ui2.lineEdit_6.setText(str(x1))
            self.ui2.lineEdit_7.setText(str(x2))
            self.ui2.lineEdit_8.setText(str(x3))
            self.ui2.lineEdit_9.setText(str(x4))
            result.append(str(x4))
            msgShow("Часть сообщения успешно передана")
            self.ui2.textEdit_2.insertPlainText(shamir.block_num_to_text(str(x4), len_keys))


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
        self.ui2.action_5.setStatusTip("Вернуться к выбору алгоритма")
        self.ui2.action.setStatusTip("Загрузить файл для шифрования")
        self.ui2.action_2.setStatusTip("Загрузить данные из файла для шифрования")
        self.ui2.action_3.setStatusTip("Сохранить полученные данные как файл")
        self.ui2.action_4.setStatusTip("Установить свою длину генерируемых ключей (от 20 знаков до 200)")

    def back(self):
        application.show()
        self.window().hide()

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 20 до 200.')
        if choice.isdigit() and int(choice) >= 20 and int(choice) <= 200:
            self.ui2.lineEdit_11.setText(choice)
            self.ui2.label_13.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина чисел задана неверно")
            return
        msgShow("Изменения успешно приняты")

    def generation_p_g(self):
        len_keys = int(self.ui2.lineEdit_11.text())
        p, g = elgamal.generation_p_g(len_keys)
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
        if p.isdigit() == False or len(p) != len_keys or g.isdigit() == False \
                or basic_algorithms.modular_pow(int(g), int(p) - 1, int(p)) != 1:
            msgShow("Введите или сгенерируйте числа p и g")
            return
        blocks = shamir.text_to_blocks_num(text, len_keys)
        for block in blocks:
            c_a, d_a = elgamal.generation_c_d(len_keys, int(p), int(g))
            c_b, d_b = elgamal.generation_c_d(len_keys, int(p), int(g))
            self.ui2.lineEdit_3.setText(str(c_a))
            self.ui2.lineEdit_4.setText(str(d_a))
            self.ui2.lineEdit_8.setText(str(c_b))
            self.ui2.lineEdit_9.setText(str(d_b))
            k, r, e = elgamal.calculated_r_e(int(block), int(g), int(p), d_b)
            self.ui2.lineEdit_5.setText(str(k))
            self.ui2.lineEdit_6.setText(str(r))
            self.ui2.lineEdit_7.setText(str(e))
            m = elgamal.get_m(e, r, int(p), c_b)
            self.ui2.lineEdit_10.setText(str(m))
            block_text = shamir.block_num_to_text(block, len_keys)
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
        self.ui2.action.setStatusTip("Загрузить данные из файла для хэширования")
        self.ui2.action_2.setStatusTip("Загрузить файл для хэширования")
        self.ui2.action_3.setStatusTip("Загрузить результат в файл")
        self.ui2.action_4.setStatusTip("Вернуться к выбору алгоритма")

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
            self.ui2.lineEdit.setText(md5.data_to_md5(text=text))
        else:
            self.ui2.lineEdit.setText(md5.data_to_md5(file_name=fname))
            self.ui2.label_3.setText("")


class SHAHashWin(QMainWindow, Ui_Form_Hash):
    def __init__(self, parent=None):
        super(SHAHashWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_Hash()
        self.ui2.setupUi(self)
        self.setWindowTitle("SHA")
        self.ui2.action_4.triggered.connect(self.back)
        self.ui2.action.triggered.connect(self.open_file)
        self.ui2.action_2.triggered.connect(self.open_file_bytes)
        self.ui2.action_3.triggered.connect(self.save_in_file)
        self.ui2.pushButton.clicked.connect(self.hash_sha1)
        self.ui2.action.setStatusTip("Загрузить данные из файла для хэширования")
        self.ui2.action_2.setStatusTip("Загрузить файл для хэширования")
        self.ui2.action_3.setStatusTip("Загрузить результат в файл")
        self.ui2.action_4.setStatusTip("Вернуться к выбору алгоритма")

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

    def hash_sha1(self):
        text = self.ui2.textEdit.toPlainText()
        fname = self.ui2.label_3.text()
        if text == '':
            msgShow("Нет данных для хэширования")
            return
        if fname == "":
            self.ui2.lineEdit.setText(sha1.data_to_sha1(text=text))
        else:
            self.ui2.lineEdit.setText(sha1.data_to_sha1(file_name=fname))
            self.ui2.label_3.setText("")


class DigSignRSAWin(QMainWindow, Ui_Form_DigSignRsa):

    def __init__(self, parent=None):
        super(DigSignRSAWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_DigSignRsa()
        self.ui2.setupUi(self)
        self.ui2.action_3.triggered.connect(self.back)
        self.ui2.pushButton.clicked.connect(self.get_digital_signature)
        self.ui2.pushButton_2.clicked.connect(self.send_data_signature)
        self.ui2.pushButton_3.clicked.connect(self.get_keys)
        self.ui2.pushButton_4.clicked.connect(self.check_signature)
        self.ui2.action.triggered.connect(self.open_file_bytes)
        self.ui2.action_2.triggered.connect(self.change_len_keys)
        self.ui2.action_5.triggered.connect(self.save_keys_signature)
        self.ui2.action_4.triggered.connect(self.download_keys_signature)
        self.ui2.action.setStatusTip("Загрузить файл для получения электронной подписи")
        self.ui2.action_2.setStatusTip("Установить свою длину генерируемых ключей (от 50 знаков до 200)")
        self.ui2.action_3.setStatusTip("Вернуться к выбору алгоритма")
        self.ui2.action_4.setStatusTip("Загрузить открытые и закрытый ключи и электронную подпись (из 3-х файлов)")
        self.ui2.action_5.setStatusTip("Сохранить открытые и закрытый ключи и электронную подпись (в 3 файла)")

    def back(self):
        application.show()
        self.window().hide()

    def get_digital_signature(self):
        text = self.ui2.textEdit.toPlainText()
        if text == "":
            msgShow("Введите или загрузите текст")
            return
        hash = str(self.ui2.comboBox.currentText())
        len_keys = self.ui2.label_13.text()
        N, d, c = digital_signature_rsa.generation_keys(int(len_keys))
        self.ui2.lineEdit.setText(str(N))
        self.ui2.lineEdit_2.setText(str(d))
        self.ui2.lineEdit_3.setText(str(c))
        s = digital_signature_rsa.get_signature(text, hash, c, N)
        self.ui2.lineEdit_4.setText(str(s))

    def send_data_signature(self):
        text = self.ui2.textEdit.toPlainText()
        signature = self.ui2.lineEdit_4.text()
        if text == "" or signature == "":
            msgShow("Получите данные с подписью для проверки")
            return
        self.ui2.textEdit_2.setText(text)
        self.ui2.lineEdit_5.setText(signature)

    def get_keys(self):
        N = self.ui2.lineEdit.text()
        d = self.ui2.lineEdit_2.text()
        if N == "" or d == "":
            msgShow("Пользователь не размещал открытые ключи")
            return
        self.ui2.lineEdit_6.setText(N)
        self.ui2.lineEdit_7.setText(d)
        return

    def check_signature(self):
        text = self.ui2.textEdit_2.toPlainText()
        s = self.ui2.lineEdit_5.text()
        d = self.ui2.lineEdit_7.text()
        N = self.ui2.lineEdit_6.text()
        if text == "" or s == "" or d == "" or N == "":
            msgShow("Вы не получили данные от пользователя")
            return
        hash = str(self.ui2.comboBox.currentText())
        if digital_signature_rsa.check_signature(text, hash, int(s), int(d), int(N)):
            self.ui2.lineEdit_8.setText("Подпись верна")
        else:
            self.ui2.lineEdit_8.setText("Подпись не верна")
        return

    def open_file_bytes(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'rb') as file:
                text = file.read()
        except FileNotFoundError:
            return
        self.ui2.textEdit.setText(str(text))

    def save_keys_signature(self):
        N = self.ui2.lineEdit.text()
        d = self.ui2.lineEdit_2.text()
        c = self.ui2.lineEdit_3.text()
        s = self.ui2.lineEdit_4.text()
        if N == "" or d == "" or c == "" or s == "":
            msgShow("Нет данных для сохранения")
            return
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых, \nзакрытого ключей и подписи через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'w+')
                file.write(N + '\n' + d)
                file.close()
                file = open(choice[1], 'w+')
                file.write(c)
                file.close()
                file = open(choice[2], 'w+')
                file.write(s)
                file.close()
            except FileNotFoundError:
                return
            msgShow("Данные успешно сохранены")
        else:
            msgShow("Сохранение не произошло")

    def download_keys_signature(self):
        len_keys = int(self.ui2.label_13.text())
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых \nзакрытого ключей и подписи через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'r')
                N = file.readline()[:-1]
                d = file.readline()
                file.close()
                if N.isdigit() == False or d.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.label_13.setText(str(len(N)))
                self.ui2.label_15.setText("Длина ключей " + str(len(N)) + " символов.")
                self.ui2.lineEdit.setText(N)
                self.ui2.lineEdit_2.setText(d)

                file = open(choice[1], 'r')
                c = file.read()
                file.close()
                if c.isdigit() == False or len(c) < len_keys:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.lineEdit_3.setText(c)

                file = open(choice[2], 'r')
                s = file.read()
                file.close()
                if s.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.lineEdit_4.setText(s)
            except FileNotFoundError:
                msgShow("Выберите существующие файлы")
                return
        return

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 50 до 200.')
        if choice.isdigit() and int(choice) >= 50 and int(choice) <= 200:
            self.ui2.label_13.setText(choice)
            self.ui2.label_15.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина ключей задана неверно")
            return
        msgShow("Изменения успешно приняты")


class DigSignElGamalWin(QMainWindow, Ui_Form_DigSignElGamal):
    def __init__(self, parent=None):
        super(DigSignElGamalWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_DigSignElGamal()
        self.ui2.setupUi(self)
        self.ui2.action_5.triggered.connect(self.back)
        self.ui2.pushButton_2.clicked.connect(self.get_digital_signature)
        self.ui2.pushButton_3.clicked.connect(self.send_data_signature)
        self.ui2.pushButton_4.clicked.connect(self.get_key)
        self.ui2.pushButton.clicked.connect(self.check_signature)
        self.ui2.action.triggered.connect(self.open_file_bytes)
        self.ui2.action_2.triggered.connect(self.download_keys_signature)
        self.ui2.action_3.triggered.connect(self.save_keys_signature)
        self.ui2.action_4.triggered.connect(self.change_len_keys)
        self.ui2.action.setStatusTip("Загрузить файл для получения электронной подписи")
        self.ui2.action_2.setStatusTip("Загрузить открытыe и закрытый ключи и электронную подпись (из 3-х файлов)")
        self.ui2.action_3.setStatusTip("Сохранить открытыe и закрытый ключи и электронную подпись (в 3 файла)")
        self.ui2.action_4.setStatusTip("Установить свою длину генерируемых ключей (от 50 знаков до 200)")
        self.ui2.action_5.setStatusTip("Вернуться к выбору алгоритма")

    def back(self):
        application.show()
        self.window().hide()

    def get_digital_signature(self):
        text = self.ui2.textEdit.toPlainText()
        if text == "":
            msgShow("Нет данных для подписи")
            return
        len_keys = int(self.ui2.label_16.text())
        hash = str(self.ui2.comboBox.currentText())
        p, g = digital_signature_elgamal.generation_p_g(len_keys)

        x, y = digital_signature_elgamal.generation_keys(p, g)
        self.ui2.lineEdit.setText(str(p))
        self.ui2.lineEdit_2.setText(str(g))
        self.ui2.lineEdit_3.setText(str(x))
        self.ui2.lineEdit_4.setText(str(y))
        r, s = digital_signature_elgamal.get_signature(text, hash, p, g, x)
        self.ui2.lineEdit_5.setText(str(r) + ' ' + str(s))

    def send_data_signature(self):
        text = self.ui2.textEdit.toPlainText()
        signature = self.ui2.lineEdit_5.text()
        if text == "" or signature == "":
            msgShow("Нет данных для отправки")
            return
        self.ui2.textEdit_2.setText(text)
        self.ui2.lineEdit_6.setText(signature)

    def get_key(self):
        p = self.ui2.lineEdit.text()
        g = self.ui2.lineEdit_2.text()
        y = self.ui2.lineEdit_4.text()
        if p == "" or g == "" or y == "":
            msgShow("Пользователь не размещал данные")
            return
        self.ui2.lineEdit_7.setText(str(p))
        self.ui2.lineEdit_8.setText(str(g))
        self.ui2.lineEdit_9.setText(str(y))

    def check_signature(self):
        text = self.ui2.textEdit_2.toPlainText()
        y = self.ui2.lineEdit_9.text()
        signature = self.ui2.lineEdit_6.text()
        p = self.ui2.lineEdit_7.text()
        g = self.ui2.lineEdit_8.text()
        if text == "" or signature == "" or p == "":
            msgShow("Не хватает данных для проверки")
            return
        r, s = signature.split(" ")
        hash = str(self.ui2.comboBox.currentText())
        if digital_signature_elgamal.check_signature(text, hash, int(y), int(r), int(s), int(p), int(g)):
            self.ui2.lineEdit_10.setText("Подпись верна")
        else:
            self.ui2.lineEdit_10.setText("Подпись не верна")

    def open_file_bytes(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'rb') as file:
                text = file.read()
        except FileNotFoundError:
            return
        self.ui2.textEdit.setText(str(text))

    def save_keys_signature(self):
        p = self.ui2.lineEdit.text()
        g = self.ui2.lineEdit_2.text()
        x = self.ui2.lineEdit_3.text()
        y = self.ui2.lineEdit_4.text()
        signature = self.ui2.lineEdit_5.text()
        if p == "" or g == "" or x == "" or y == "":
            msgShow("Нет данных для сохранения")
            return
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых, \nзакрытого ключей и подписи через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'w+')
                file.write(p + '\n' + g + '\n' + y)
                file.close()
                file = open(choice[1], 'w+')
                file.write(x)
                file.close()
                file = open(choice[2], 'w+')
                file.write(signature)
                file.close()
            except FileNotFoundError:
                return
            msgShow("Данные успешно сохранены")
        else:
            msgShow("Сохранение не произошло")

    def download_keys_signature(self):
        len_keys = int(self.ui2.label_16.text())
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для открытых \nзакрытого ключей и подписи через пробел')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'r')
                p = file.readline()[:-1]
                g = file.readline()[:-1]
                y = file.readline()
                file.close()
                if p.isdigit() == False or g.isdigit() == False or y.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.label_16.setText(str(len(p)))
                self.ui2.label_15.setText("Длина ключей " + str(len(p)) + " символов.")
                self.ui2.lineEdit.setText(p)
                self.ui2.lineEdit_2.setText(g)
                self.ui2.lineEdit_4.setText(y)

                file = open(choice[1], 'r')
                x = file.read()
                file.close()
                if x.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.lineEdit_3.setText(x)

                file = open(choice[2], 'r')
                signature = file.read()
                file.close()
                if signature.replace(' ', '').isdigit() == False or len(signature.split(" ")) != 2:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.lineEdit_5.setText(signature)
            except FileNotFoundError:
                msgShow("Выберите существующие файлы")
                return
        return

    def change_len_keys(self):
        choice, ok = QInputDialog.getText(self, 'Change len keys ',
                                          'Укажите новую длину для ключей от 50 до 200.')
        if choice.isdigit() and int(choice) >= 50 and int(choice) <= 200:
            self.ui2.label_16.setText(choice)
            self.ui2.label_15.setText("Длина ключей " + choice + " символов.")
        else:
            msgShow("Длина ключей задана неверно")
            return
        msgShow("Изменения успешно приняты")


class DSAWin(QMainWindow, Ui_Form_DSA):

    def __init__(self, parent=None):
        super(DSAWin, self).__init__(parent)
        self.setupUi(self)
        self.ui2 = Ui_Form_DSA()
        self.ui2.setupUi(self)
        self.ui2.pushButton.clicked.connect(self.gener_p_q_g)
        self.ui2.pushButton_2.clicked.connect(self.gener_keys)
        self.ui2.pushButton_3.clicked.connect(self.get_digital_signature)
        self.ui2.pushButton_4.clicked.connect(self.send_data_signature)
        self.ui2.pushButton_5.clicked.connect(self.get_open_key)
        self.ui2.pushButton_6.clicked.connect(self.check_signature)
        self.ui2.action.triggered.connect(self.open_file_bytes)
        self.ui2.action.setStatusTip("Загрузить файл для получения электронной подписи")
        self.ui2.action_2.triggered.connect(self.save_numbs_keys)
        self.ui2.action_2.setStatusTip("Сохранить общие числа, открытый и закрытый ключи (2 файла)")
        self.ui2.action_3.triggered.connect(self.save_signature)
        self.ui2.action_3.setStatusTip("Сохранить подпись")
        self.ui2.action_4.triggered.connect(self.download_numbs_keys)
        self.ui2.action_4.setStatusTip("Загрузить общие числа, открытый и закрытый ключи")
        self.ui2.action_5.triggered.connect(self.download_signature)
        self.ui2.action_5.setStatusTip("Загрузить подпись")
        self.ui2.action_6.triggered.connect(self.back)
        self.ui2.action_6.setStatusTip("Вернуться к выбору алгоритма")

    def back(self):
        application.show()
        self.window().hide()

    def gener_p_q_g(self):
        data = self.ui2.textEdit_4.toPlainText()
        if data == "":
            msgShow("Введите данные")
            return

        self.ui2.label_12.setText("Выполняется генерация числа")
        self.ui2.label_13.setText("Выполняется генерация числа")
        self.ui2.label_14.setText("Выполняется генерация числа")
        self.ui2.label_12.hide()
        self.ui2.label_13.hide()
        self.ui2.label_14.hide()

        self.ui2.label_13.show()
        start_time = time.time()
        q = dsa.generation_q(sha1.data_to_sha1(data))
        self.ui2.label_13.setText("Число сгенерировано за " + str(time.time() - start_time)[:5] + " сек.")
        self.ui2.textEdit_2.setText(str(q))

        self.ui2.label_12.show()
        self.repaint()
        start_time = time.time()
        p = dsa.generation_p(q)
        self.ui2.label_12.setText("Число сгенерировано за " + str(time.time() - start_time)[:5] + " сек.")
        self.ui2.textEdit.setText(str(p))

        self.ui2.label_14.show()
        self.repaint()
        start_time = time.time()
        g = dsa.generation_g(p, q)
        self.ui2.label_14.setText("Число сгенерировано за " + str(time.time() - start_time)[:5] + " сек.")
        self.ui2.textEdit_3.setText(str(g))

    def gener_keys(self):
        p = self.ui2.textEdit.toPlainText()
        q = self.ui2.textEdit_2.toPlainText()
        g = self.ui2.textEdit_3.toPlainText()
        if p == '' or q == '' or g == '':
            msgShow("Сгенерируйте общие числа")
            return
        x, y = dsa.generation_keys(int(p), int(q), int(g))

        self.ui2.textEdit_5.setText(str(y))
        self.ui2.textEdit_6.setText(str(x))

    def get_digital_signature(self):
        data = self.ui2.textEdit_4.toPlainText()
        if data == "":
            msgShow("Нет данных для подписи")
            return
        p = self.ui2.textEdit.toPlainText()
        q = self.ui2.textEdit_2.toPlainText()
        g = self.ui2.textEdit_3.toPlainText()
        if p == "" or q == "" or g == "":
            msgShow("Общие числа не сгенерированы")
            return
        x = self.ui2.textEdit_6.toPlainText()
        if x == "":
            msgShow("Ключи не сгенерированы")
            return
        r, s = dsa.get_signature(data, int(p), int(q), int(g), int(x))
        self.ui2.textEdit_7.setText(str(r) + " " + str(s))

    def send_data_signature(self):
        data = self.ui2.textEdit_4.toPlainText()
        signature = self.ui2.textEdit_7.toPlainText()
        sign = signature.split(" ")
        if data == "" or signature == "" or len(sign) != 2 or sign[0].isdigit() == False \
                or sign[1].isdigit() == False:
            msgShow("Нет данных для отправки или они не верны")
            return
        self.ui2.textEdit_8.setText(data)
        self.ui2.textEdit_9.setText(signature)
        return

    def get_open_key(self):
        key = self.ui2.textEdit_5.toPlainText()
        if key == "":
            msgShow("Ключи не были сгенерированы")
            return
        self.ui2.textEdit_10.setText(key)
        return

    def check_signature(self):
        data = self.ui2.textEdit_8.toPlainText()
        signature = self.ui2.textEdit_9.toPlainText()
        sign = signature.split(" ")
        y = self.ui2.textEdit_10.toPlainText()
        if data == "" or signature == "" or len(sign) != 2 or y == "" or sign[0].isdigit() == False \
                or sign[1].isdigit() == False:
            msgShow("Данные не получены или не верны")
            return
        r, s = sign[0], sign[1]
        p = self.ui2.textEdit.toPlainText()
        q = self.ui2.textEdit_2.toPlainText()
        g = self.ui2.textEdit_3.toPlainText()
        if p == "" or q == "" or g == "":
            msgShow("Общие числа не сгенерированы")
            return
        if dsa.check_signature(data, int(p), int(q), int(g), int(r), int(s), int(y)):
            self.ui2.textEdit_11.setText("Подпись верна")
        else:
            self.ui2.textEdit_11.setText("Подпись не верна")
        return

    def open_file_bytes(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        try:
            with open(fname, 'rb') as file:
                text = file.read()
        except FileNotFoundError:
            return
        self.ui2.textEdit_4.setText(str(text))

    def save_numbs_keys(self):
        p = self.ui2.textEdit.toPlainText()
        q = self.ui2.textEdit_2.toPlainText()
        g = self.ui2.textEdit_3.toPlainText()
        x = self.ui2.textEdit_6.toPlainText()
        y = self.ui2.textEdit_5.toPlainText()

        if p == "" or g == "" or q == "" or x == "" or y == "":
            msgShow("Нет данных для сохранения")
            return
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для общих чисел, открытого и закрытого ключей через пробел (3 файла)')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'w+')
                file.write(p + '\n' + q + '\n' + g)
                file.close()
                file = open(choice[1], 'w+')
                file.write(y)
                file.close()
                file = open(choice[2], 'w+')
                file.write(x)
                file.close()
            except FileNotFoundError:
                return
            msgShow("Данные успешно сохранены")
        else:
            msgShow("Сохранение не произошло")

    def download_numbs_keys(self):
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имена файлов для общих чисел, открытого и закрытого ключей через пробел (3 файла)')
        if ok and choice != '':
            choice = choice.split()
            if len(choice) != 3:
                msgShow("Введите 3 файла")
                return
            try:
                file = open(choice[0], 'r')
                p = file.readline()[:-1]
                q = file.readline()[:-1]
                g = file.readline()
                file.close()
                if p.isdigit() == False or q.isdigit() == False or g.isdigit() == False or dsa.check_p_q_g(int(p), int(q), int(g)) == False:
                    msgShow("Данные не удовлетворяют формату")
                    return

                self.ui2.textEdit.setText(p)
                self.ui2.textEdit_2.setText(q)
                self.ui2.textEdit_3.setText(g)

                file = open(choice[1], 'r')
                y = file.read()
                file.close()
                if y.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.textEdit_10.setText(y)
                self.ui2.textEdit_5.setText(y)

                file = open(choice[2], 'r')
                x = file.read()
                file.close()
                if x.isdigit() == False or 0 > int(x) > int(q):
                    msgShow("Данные не удовлетворяют формату")
                    return
                self.ui2.textEdit_6.setText(x)
            except FileNotFoundError:
                msgShow("Выберите существующие файлы")
                return
        return

    def save_signature(self):
        signature = self.ui2.textEdit_7.toPlainText()
        sign = signature.split(" ")
        if  signature == "" or len(sign) != 2 or sign[0].isdigit() == False \
                or sign[1].isdigit() == False:
            msgShow("Нет данных для сохранения или они не верны")
            return
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имя для файла с подписью)')
        if ok and choice != '':
            try:
                file = open(choice, 'w+')
                file.write(sign[0]+"\n"+sign[1])
                file.close()
            except FileNotFoundError:
                return
            msgShow("Данные успешно сохранены")
        else:
            msgShow("Сохранение не произошло")
        return

    def download_signature(self):
        choice, ok = QInputDialog.getText(self, 'File names ',
                                          'Укажите имя файла с подписью')
        if ok and choice != '':
            try:
                file = open(choice, 'r')
                r = file.readline()[:-1]
                s = file.readline()
                file.close()
                if r.isdigit() == False or s.isdigit() == False:
                    msgShow("Данные не удовлетворяют формату")
                    return

                self.ui2.textEdit_7.setText(r + " " + s)
                self.ui2.textEdit_9.setText(r+" "+s)

            except FileNotFoundError:
                msgShow("Выберите существующие файлы")
                return
        return

app = QApplication([])
application = MainWin()
application.show()


def msgShow(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()


sys.exit(app.exec())
