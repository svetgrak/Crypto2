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
    return text_with_padding + bits_len_mess


def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF


def init_buffer():
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    return h0, h1, h2, h3, h4


def print_sha1(buffer):
    result = ''
    for numb in buffer:
        numb = numb[2:].rjust(8, '0')
        result += numb
    return result

def data_to_sha1 (text="", file_name=""):
    if file_name == "":
        text = bytearray(text.encode())
    else:
        file = open(file_name, "rb")
        text = file.read()

    text = text_to_bit(text)

    text_with_padding = add_padding_bits(text)
    text_bits = add_len_message(text, text_with_padding)

    h0, h1, h2, h3, h4 = init_buffer()

    array_text_bits = [text_bits[i: i + 512] for i in range(0, len(text_bits), 512)]
    for chunk in array_text_bits:

        words = [int(chunk[i: i + 32], 2) for i in range(0, 512, 32)]
        for i in range(16, 80):
            # (w[i-3] xor w[i-8] xor w[i-14] xor w[i-16])
            words.append(left_rotate(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if 0 <= i <= 19:
                f = d ^ (b & (c ^ d))
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            f = (left_rotate(a, 5) + f + e + k + words[i]) % pow(2, 32)
            e, d, c, b, a = d, c, left_rotate(b, 30), a, f

        h0 = (h0 + a) % pow(2, 32)
        h1 = (h1 + b) % pow(2, 32)
        h2 = (h2 + c) % pow(2, 32)
        h3 = (h3 + d) % pow(2, 32)
        h4 = (h4 + e) % pow(2, 32)

    return (print_sha1([hex(h0), hex(h1), hex(h2), hex(h3), hex(h4)]))
