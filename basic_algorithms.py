def modular_pow(a, x, p):
    x = list(reversed(bin(x)))[:-2]
    s = a
    y = 1
    for i in range(len(x)):
        if int(x[i]) == 1:
            y = (y * s) % p
        s = (s * s) % p
    return y


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


def gcd(a, b):
    return (egcd(a, b)[0])


def invert(x, p):
    return (egcd(x, p)[2])
