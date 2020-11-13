import basic_algorithms
import rsa
import md5
import sha1


def generation_keys(len_keys):
    while True:
        p = rsa.generation_prime_numb(len_keys / 2)
        q = rsa.generation_prime_numb(len_keys / 2)
        N = p * q
        if len(str(N))<len_keys:
            continue
        d = 65537
        c = basic_algorithms.egcd(d, ((p - 1) * (q - 1)))[1]
        if c > 0 and len(str(c)) == len_keys and c < N:
            break
    return N, d, c


def get_signature(text="", hash="md5", c=0, N=0):
    if hash == "md5":
        y = md5.data_to_md5(text)
    elif hash == "sha1":
        y = sha1.data_to_sha1(text)
    s = basic_algorithms.modular_pow(int(y, 16), c, N)
    return s


def check_signature(text="", hash="md5", s=0, d=0, N=0):
    if hash == "md5":
        y = md5.data_to_md5(text)
    elif hash == "sha1":
        y = sha1.data_to_sha1(text)
    w = basic_algorithms.modular_pow(s, d, N)
    if hex(w)[2:] == y:
        return True
    return False
