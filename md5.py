import math


def text_to_bit(bytes):
    return ''.join([bin(byte)[2:].rjust(8, '0') for byte in bytes])


def add_padding_bits(bits):
    bits_with_padding = bits + '1'
    if len(bits) % 512 == 448:
        bits_with_padding.ljust(960, '0')
    else:
        while len(bits_with_padding) % 512 != 448:
            bits_with_padding += '0'
    return bits_with_padding


def add_len_message(bits_massage, text_with_padding):
    bits_len_mess = str(bin(len(bits_massage)))[2:][-64:].rjust(64, '0')
    bits_array = [bits_len_mess[i:i + 8] for i in range(0, 64, 8)]
    for byte in reversed(bits_array):
        text_with_padding += byte
    return text_with_padding


def init_buffer():
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    T = [int(math.pow(2, 32) * abs(math.sin(n))) for n in range(1, 65)]
    return A, B, C, D, T


def fun_F(X, Y, Z):
    return (X & Y) | (~X & Z)


def fun_G(X, Y, Z):
    return (X & Z) | (~Z & Y)


def fun_H(X, Y, Z):
    return (X ^ Y ^ Z)


def fun_I(X, Y, Z):
    return (Y ^ (~Z | X))


def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF


def print_md5(buffer):
    result = []
    for numb in buffer:
        numb = numb[2:].rjust(8, '0')
        numb = [numb[i:i + 2] for i in range(0, len(numb), 2)]
        for byte in reversed(numb):
            result.append(byte)
    return ''.join(result)


def str_bits_to_int(bits):
    bits = reversed([bits[i:i + 8] for i in range(0, 32, 8)])
    return int(''.join(bits), 2)


s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15,
     21]


def data_to_md5(text="", file_name=""):
    if file_name == "":
        text = bytearray(text.encode())
    else:
        file = open(file_name, "rb")
        text = file.read()

    text = text_to_bit(text)

    text_with_padding = add_padding_bits(text)
    text_bits = add_len_message(text, text_with_padding)

    a0, b0, c0, d0, T = init_buffer()
    array_text_bits = [text_bits[i: i + 512] for i in range(0, len(text_bits), 512)]

    for chunk in array_text_bits:
        words = [str_bits_to_int(chunk[i: i + 32]) for i in range(0, 512, 32)]

        A, B, C, D = a0, b0, c0, d0
        for i in range(64):
            if i >= 0 and i <= 15:
                F = fun_F(B, C, D)
                g = i
            elif i >= 16 and i <= 31:
                F = fun_G(B, C, D)
                g = (5 * i + 1) % 16
            elif i >= 32 and i <= 47:
                F = fun_H(B, C, D)
                g = (3 * i + 5) % 16
            elif i >= 48 and i <= 63:
                F = fun_I(B, C, D)
                g = (7 * i) % 16

            F = F + A + T[i] + words[g]
            A = D
            D = C
            C = B
            B = (B + (left_rotate(F, s[i]))) % pow(2, 32)

        a0 = (a0 + A) % pow(2, 32)
        b0 = (b0 + B) % pow(2, 32)
        c0 = (c0 + C) % pow(2, 32)
        d0 = (d0 + D) % pow(2, 32)

    md5_hex = print_md5([hex(a0), hex(b0), hex(c0), hex(d0)])
    return (md5_hex)
