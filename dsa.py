import random
import sha1
import rsa
import basic_algorithms
import time
import numpy


def generation_prime(len_bits):
    while (True):
        prime_number = numpy.long(random.randint(2 ** (len_bits - 1),
                                                 2 ** len_bits))
        if rsa.miller_rabin(prime_number) == None:
            if rsa.ferma(prime_number) == True:
                return (prime_number)


def is_prime(number):
    if rsa.miller_rabin(number) == None:
        if rsa.ferma(number) == True:
            return True
    return False

def generation_q(h_data):
    while True:
        q = generation_prime(160)
        if q > int(h_data, 16):
            break
    return q

def generation_p(q):
    while (True):
        b = random.randint(2 ** (1024 - 161), 2 ** (1024 - 160))
        p = (b * q) + 1
        if is_prime(p) and len(bin(p)) - 2 == 1024:
            break
    return p

def generation_g(p,q):
    while True:
        h = random.randint(1, p - 1)
        g = basic_algorithms.modular_pow(h, (p - 1) // q, p)
        if basic_algorithms.modular_pow(g, q, p) == 1:
            break
    return g

def generation_p_q_g(h_data):
    q = generation_q(h_data)
    p = generation_p(q)
    g = generation_g(p,q)
    return p, q, g

def generation_keys(p,q,g):
    x = random.randint(0, q)
    y = basic_algorithms.modular_pow(g, x, p)
    return x,y

def get_signature(data, p, q, g, x):
    h_data = sha1.data_to_sha1(data)
    while True:
        k = random.randint(0, q)
        r = (basic_algorithms.modular_pow(g, k, p) % q)
        s = (basic_algorithms.invert(k, q) * (int(h_data, 16) + x * r)) % q
        if r != 0 and s != 0:
            break
    return r, s

def check_signature(data,p,q,g,r,s,y):
    h_data = sha1.data_to_sha1(data)
    if 0 > r > q or 0 > s > q:
        return False
    w = basic_algorithms.invert(s, q)
    u_1 = (int(h_data, 16) * w) % q
    u_2 = (r * w) % q
    v = (basic_algorithms.modular_pow(g, u_1, p) * basic_algorithms.modular_pow(y, u_2, p) % p) % q
    if v == r:
        return True
    return False

def check_p_q_g(p, q, g):
    if len(bin(p))-2 != 1024 or len(bin(q))-2 != 160:
        return False
    if is_prime(p) == False or is_prime(q) == False:
        return False
    if (p - 1) % q != 0:
        return False
    if basic_algorithms.modular_pow(g, q, p) != 1:
        return False


    return True



'''
text = "hello"
file = "i.webp"
h_data = sha1.data_to_sha1(text)
p, q, g = generation_p_q_g(h_data)



x_1 = random.randint(0, q)
y_1 = basic_algorithms.modular_pow(g, x_1, p)

x_2 = random.randint(0, q)
y_2 = basic_algorithms.modular_pow(g, x_2, p)



while True:
    k = random.randint(0, q)
    r = (basic_algorithms.modular_pow(g, k, p) % q)
    s = (basic_algorithms.invert(k,q) * (int(h_data, 16) + x_1 * r)) % q
    if r != 0 and s != 0:
        break

w = basic_algorithms.invert(s, q)
u_1 = (int(h_data, 16) * w) % q
u_2 = (r * w) % q
v = (basic_algorithms.modular_pow(g, u_1, p) * basic_algorithms.modular_pow(y_1, u_2, p) % p) % q
if v == r:
    print(x_1,y_1)
else:
    print(False)


'''

