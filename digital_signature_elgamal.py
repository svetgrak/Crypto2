import elgamal
import random
import basic_algorithms
import md5
import sha1


def generation_p_g(len_keys):
    return elgamal.generation_p_g(len_keys)


def generation_keys(p, g):
    x = random.randint(1, p - 1)
    y = basic_algorithms.modular_pow(g, x, p)
    return x, y


def get_signature(text, hash, p, g, x):
    if hash == "md5":
        h = md5.data_to_md5(text)
    elif hash == "sha1":
        h = sha1.data_to_sha1(text)

    while True:
        k = random.randint(1, p - 1)
        if basic_algorithms.gcd(k, p - 1) == 1:
            break

    r = basic_algorithms.modular_pow(g, k, p)
    u = (int(h, 16) - x * r) % (p - 1)
    s = (basic_algorithms.invert(k, p - 1) * u) % (p - 1)
    return r, s

def check_signature(text, hash, y, r, s, p, g):
    if hash == "md5":
        h = md5.data_to_md5(text)
    elif hash == "sha1":
        h = sha1.data_to_sha1(text)
    if (basic_algorithms.modular_pow(y, r, p) * basic_algorithms.modular_pow(r,s,p)) % p == basic_algorithms.modular_pow(g,int(h,16),p):
        return True
    else:
        return False

