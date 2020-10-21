import basic_algorithms
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog

def ferma(n):
    if n == 2: return True
    for i in range(0, 100):
        a = random.randint(2, n - 1)
        if basic_algorithms.gcd(a, n) != 1: return False
        if basic_algorithms.modular_pow(a, n - 1, n) != 1: return False
    return True

def miller_rabin(n, s=100):
    for j in range(1, s + 1):
        a = random.randint(1, n - 1)
        b = genr(n - 1)
        d = 1
        for i in range(len(b) - 1, -1, -1):
            x = d
            d = (d * d) % n
            if d == 1 and x != 1 and x != n - 1:
                return False
            if b[i] == 1:
                d = (d * a) % n
                if d != 1:
                    return False
                return True

def genr(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n /= 2
        return r

def generation_prime_numb(len_numb):
    while (True):
        prime_number = random.randint(10 ** (len_numb - 1),
                                      10 ** len_numb)
        if miller_rabin(prime_number) == None:
            if ferma(prime_number) == True:
                return (prime_number)

def generation_keys(len_keys):
    while (True):
        p = generation_prime_numb(len_keys / 2)
        q = generation_prime_numb(len_keys / 2)
        n = p * q
        #e = generation_prime_numb(len_keys)
        e = 65537
        if e > n:
            continue
        d = basic_algorithms.egcd(e, ((p - 1) * (q - 1)))[1]
        if d > 0 and len(str(d)) == len_keys:
            #print("open keys: ", e, n)
            #print("close key: ", d)
            break

    return (e, n, d)

def text_in_numb(text):
    result = ''
    for ch in text:
        var = str(ord(ch)).rjust(4, '0')
        result += var
    return result

def encrypt(text, e, n):
    len_block = len(str(n))//4
    blocks = [text[i:i + len_block] for i in range(0, len(text), len_block)]
    for i in range(len(blocks)):
        blocks[i] = text_in_numb(blocks[i])
    result = ''
    print(blocks)
    encr_text = [basic_algorithms.modular_pow(int(blocks[i]), e, n) for i in range(len(blocks))]
    for block in encr_text:
        result += str(block) + ' '
    return result

def decrypt(text, d, n):
    text = text.split()
    decrypt_text = [str(basic_algorithms.modular_pow(int(text[i]), d, n)) for i in range(len(text))]
    print(decrypt_text)
    for i in range(len(decrypt_text)):
        decrypt_text[i] = decrypt_text[i].rjust(((len(str(n))//4)*4),'0')
    result = ''.join(decrypt_text)
    result_text = ''
    for i in range(len(result) // 4):
        var = int(result[i * 4:(i + 1) * 4])
        if var != 0:
            result_text += chr(var)
    return result_text

def text_to_byte(text):
    result = []
    for ch in text:
        while(True):
            if int(ch) > 255:
                new_byte = int(ch[:3])
                if new_byte > 255:
                    new_byte = int(ch[:2])
                    ch = ch[2:]
                else:
                    ch = ch[3:]
                result.append(bytes([new_byte]))
            else:
                result.append(bytes([int(ch)]))
                break
    return result



