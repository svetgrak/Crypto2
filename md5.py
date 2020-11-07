import math


def text_to_bit(bytes):
    return ''.join([bin(byte)[2:].rjust(8,'0') for byte in bytes])

def add_padding_bits(bits):
    bits_with_padding = bits + '1'
    if len(bits) % 512 == 448:
        bits_with_padding.ljust(960,'0')
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
        numb = numb[2:].rjust(8,'0')
        numb = [numb[i:i + 2] for i in range(0, len(numb), 2)]
        for byte in reversed(numb):
            result.append(byte)
    return ''.join(result)


def str_bits_to_int(bits):

    bits = reversed([bits[i:i+8] for i in range(0,32,8)])
    return int(''.join(bits),2)


s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15,
     21]

def text_to_hash(text="",file_name=""):
    if file_name == "":
        text = bytearray(text.encode())
    else:
        file = open(file_name,"rb")
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
            if i >= 0 and i <=15:
                F = fun_F(B, C, D)
                g = i
            elif i >= 16 and i <=31:
                F = fun_G(B, C, D)
                g = (5*i+1)%16
            elif i >= 32 and i <=47:
                F = fun_H(B, C, D)
                g = (3*i+5)%16
            elif i >= 48 and i <=63:
                F = fun_I(B, C, D)
                g = (7*i)%16

            F = F + A + T[i] + words[g]
            A = D
            D = C
            C = B
            B = (B + (left_rotate(F,s[i])))%pow(2,32)

        a0 = (a0 + A)%pow(2,32)
        b0 = (b0 + B)%pow(2,32)
        c0 = (c0 + C)%pow(2,32)
        d0 = (d0 + D)%pow(2,32)

    md5_hex = print_md5([hex(a0),hex(b0),hex(c0),hex(d0)])
    return (md5_hex)




'''

A,B,C,D,T = init_buffer()
array_text_bits = [text_bits[i: i + 512] for i in range(0, len(text_bits), 512)]

for chunk in array_text_bits:
    AA, BB, CC, DD = A, B, C, D
    words = [str_bits_to_int(chunk[i: i + 32]) for i in range(0, 512, 32)]
    print(words)
    #  Round 1
    #  [ABCD k s i] ->> A = B + ((A + Fun(b,c,d) + words[k] + T[i] << s)
    A = (B + ((A + fun_F(B, C, D) + words[0] + T[0]) << 7)) % pow(2, 32)
    D = (A + ((D + fun_F(A, B, C) + words[1] + T[1]) << 12)) % pow(2, 32)
    C = (D + ((C + fun_F(D, A, B) + words[2] + T[2]) << 17)) % pow(2, 32)
    B = (C + ((B + fun_F(C, D, A) + words[3] + T[3]) << 22)) % pow(2, 32)

    A = (B + ((A + fun_F(B, C, D) + words[4]+ T[4]) << 7)) % pow(2, 32)
    D = (A + ((D + fun_F(A, B, C) + words[5] + T[5]) << 12)) % pow(2, 32)
    C = (D + ((C + fun_F(D, A, B) + words[6] + T[6]) << 17)) % pow(2, 32)
    B = (C + ((B + fun_F(C, D, A) + words[7]+ T[7]) << 22)) % pow(2, 32)

    A = (B + ((A + fun_F(B, C, D) + words[8] + T[8]) << 7)) % pow(2, 32)
    D = (A + ((D + fun_F(A, B, C) + words[9] + T[9]) << 12)) % pow(2, 32)
    C = (D + ((C + fun_F(D, A, B) + words[10] + T[10]) << 17)) % pow(2, 32)
    B = (C + ((B + fun_F(C, D, A) + words[11] + T[11]) << 22)) % pow(2, 32)

    A = (B + ((A + fun_F(B, C, D) + words[12] + T[12]) << 7)) % pow(2, 32)
    D = (A + ((D + fun_F(A, B, C) + words[13] + T[13]) << 12)) % pow(2, 32)
    C = (D + ((C + fun_F(D, A, B) + words[14] + T[14]) << 17)) % pow(2, 32)
    B = (C + ((B + fun_F(C, D, A) + words[15] + T[15]) << 22)) % pow(2, 32)

    # Round 2
    A = (B + ((A + fun_G(B, C, D) + words[1] + T[16]) << 5)) % pow(2, 32)
    D = (A + ((D + fun_G(A, B, C) + words[6] + T[17]) << 9)) % pow(2, 32)
    C = (D + ((C + fun_G(D, A, B) + words[11] + T[18]) << 14)) % pow(2, 32)
    B = (C + ((B + fun_G(C, D, A) + words[0] + T[19]) << 20)) % pow(2, 32)

    A = (B + ((A + fun_G(B, C, D) + words[5] + T[20]) << 5)) % pow(2, 32)
    D = (A + ((D + fun_G(A, B, C) + words[10] + T[21]) << 9)) % pow(2, 32)
    C = (D + ((C + fun_G(D, A, B) + words[15] + T[22]) << 14)) % pow(2, 32)
    B = (C + ((B + fun_G(C, D, A) + words[4] + T[23]) << 20)) % pow(2, 32)

    A = (B + ((A + fun_G(B, C, D) + words[9] + T[24]) << 5)) % pow(2, 32)
    D = (A + ((D + fun_G(A, B, C) + words[14] + T[25]) << 9)) % pow(2, 32)
    C = (D + ((C + fun_G(D, A, B) + words[3] + T[26]) << 14)) % pow(2, 32)
    B = (C + ((B + fun_G(C, D, A) + words[8] + T[27]) << 20)) % pow(2, 32)

    A = (B + ((A + fun_G(B, C, D) + words[13] + T[28]) << 5)) % pow(2, 32)
    D = (A + ((D + fun_G(A, B, C) + words[2] + T[29]) << 9)) % pow(2, 32)
    C = (D + ((C + fun_G(D, A, B) + words[7] + T[30]) << 14)) % pow(2, 32)
    B = (C + ((B + fun_G(C, D, A) + words[12] + T[31]) << 20)) % pow(2, 32)

    # Round 3
    A = (B + ((A + fun_H(B, C, D) + words[5] + T[32]) << 4)) % pow(2, 32)
    D = (A + ((D + fun_H(A, B, C) + words[8] + T[33]) << 11)) % pow(2, 32)
    C = (D + ((C + fun_H(D, A, B) + words[11] + T[34]) << 16)) % pow(2, 32)
    B = (C + ((B + fun_H(C, D, A) + words[14] + T[35]) << 23)) % pow(2, 32)

    A = (B + ((A + fun_H(B, C, D) + words[1] + T[36]) << 4)) % pow(2, 32)
    D = (A + ((D + fun_H(A, B, C) + words[4] + T[37]) << 11)) % pow(2, 32)
    C = (D + ((C + fun_H(D, A, B) + words[7] + T[38]) << 16)) % pow(2, 32)
    B = (C + ((B + fun_H(C, D, A) + words[10] + T[39]) << 23)) % pow(2, 32)

    A = (B + ((A + fun_H(B, C, D) + words[13] + T[40]) << 4)) % pow(2, 32)
    D = (A + ((D + fun_H(A, B, C) + words[0] + T[41]) << 11)) % pow(2, 32)
    C = (D + ((C + fun_H(D, A, B) + words[3] + T[42]) << 16)) % pow(2, 32)
    B = (C + ((B + fun_H(C, D, A) + words[6] + T[43]) << 23)) % pow(2, 32)

    A = (B + ((A + fun_H(B, C, D) + words[9] + T[44]) << 4)) % pow(2, 32)
    D = (A + ((D + fun_H(A, B, C) + words[12] + T[45]) << 11)) % pow(2, 32)
    C = (D + ((C + fun_H(D, A, B) + words[15] + T[46]) << 16)) % pow(2, 32)
    B = (C + ((B + fun_H(C, D, A) + words[2]+ T[47]) << 23)) % pow(2, 32)

    # Round 4
    A = (B + ((A + fun_I(B, C, D) + words[0] + T[48]) << 6)) % pow(2, 32)
    D = (A + ((D + fun_I(A, B, C) + words[7] + T[49]) << 10)) % pow(2, 32)
    C = (D + ((C + fun_I(D, A, B) + words[14] + T[50]) << 15)) % pow(2, 32)
    B = (C + ((B + fun_I(C, D, A) + words[5] + T[51]) << 21)) % pow(2, 32)

    A = (B + ((A + fun_I(B, C, D) + words[12] + T[52]) << 6)) % pow(2, 32)
    D = (A + ((D + fun_I(A, B, C) + words[3] + T[53]) << 10)) % pow(2, 32)
    C = (D + ((C + fun_I(D, A, B) + words[10] + T[54]) << 15)) % pow(2, 32)
    B = (C + ((B + fun_I(C, D, A) + words[1] + T[55]) << 21)) % pow(2, 32)

    A = (B + ((A + fun_I(B, C, D) + words[8] + T[56]) << 6)) % pow(2, 32)
    D = (A + ((D + fun_I(A, B, C) + words[15] + T[57]) << 10)) % pow(2, 32)
    C = (D + ((C + fun_I(D, A, B) + words[6] + T[58]) << 15)) % pow(2, 32)
    B = (C + ((B + fun_I(C, D, A) + words[13] + T[59]) << 21)) % pow(2, 32)

    A = (B + ((A + fun_I(B, C, D) + words[4] + T[60]) << 6)) % pow(2, 32)
    D = (A + ((D + fun_I(A, B, C) + words[11] + T[61]) << 10)) % pow(2, 32)
    C = (D + ((C + fun_I(D, A, B) + words[2] + T[62]) << 15)) % pow(2, 32)
    B = (C + ((B + fun_I(C, D, A) + words[9] + T[63]) << 21)) % pow(2, 32)

    A = (A + AA) % pow(2, 32)
    B = (B + BB) % pow(2, 32)
    C = (C + CC) % pow(2, 32)
    D = (D + DD) % pow(2, 32)

print(hex(A))
print(hex(B))
print(hex(C))
print(hex(D))
print("true hex = 99b1ff8f11781541f7f89f9bd41c4a17")
'''














