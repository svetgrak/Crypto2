import rsa
import shamir
import random
import basic_algorithms

def generation_p_g(len_keys):
    p = rsa.generation_prime_numb(len_keys)
    while True:
        g = random.randint(10 ** (len_keys - 1), 10 ** len_keys)
        if basic_algorithms.modular_pow(g, p - 1, p) == 1:
            break
    return(p, g)


def generation_c_d(len_keys,p,g):
    while True:
        c = random.randint(10 ** (len_keys - 1), 10 ** len_keys)
        if c < p - 1 and basic_algorithms.gcd(c, p - 1):
            d = basic_algorithms.modular_pow(g, c, p)
            break
    return c,d

def calculated_r_e(text,g,p,d):

    k = random.randint(1, p-2)
    r = basic_algorithms.modular_pow(g, k, p)
    e = (text * basic_algorithms.modular_pow(d, k, p)) % p
    return k,r,e

def get_m(e,r,p,c):
    return (e*basic_algorithms.modular_pow(r,(p-1)-c,p))%p


'''
text = 123456
len_keys = 20

p = rsa.generation_prime_numb(len_keys)
while True:
    g = random.randint(10 ** (len_keys - 1), 10 ** len_keys)
    if basic_algorithms.modular_pow(g,p-1,p) == 1:
        break
print(p,g)

c_a,d_a = generation_c_d(len_keys)
print(c_a,d_a)
c_b,d_b = generation_c_d(len_keys)
print(c_b,d_b)
while True:
    k = random.randint(10 ** (len_keys - 1), 10 ** len_keys)
    if k < p-1:
        break

r = basic_algorithms.modular_pow(g,k,p)
e = (text * basic_algorithms.modular_pow(d_b,k,p))%p
m= (e*basic_algorithms.modular_pow(r,(p-1)-c_b,p))%p
print(m)
'''