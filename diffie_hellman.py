import random
from rsa import generation_prime_numb, ferma, miller_rabin
import basic_algorithms

def check_prime(num):
    if miller_rabin(num) == None:
        if ferma(num) == True:
            return True
    return False

def generation_a_g_p(len_keys):
    a = random.randint(10 ** (len_keys - 1), 10 ** len_keys)
    while True:
        p = generation_prime_numb(len_keys)
        if check_prime((p - 1) // 2):
            break
    while True:
        g = generation_prime_numb(len_keys)
        if basic_algorithms.modular_pow(g, p - 1, p) == 1:
            break
    return (a,g,p)

def generation_b(len_keys):
    return random.randint(10 ** (len_keys - 1),10 ** len_keys)

def calculated(a,g,p):
    return basic_algorithms.modular_pow(a,g,p)


'''
len_keys = 50
a = random.randint(10 ** (len_keys - 1),10 ** len_keys)
while True:
    p = generation_prime_numb(len_keys)
    if check_prime((p-1)//2):
        break
while True:
    g = generation_prime_numb(len_keys)
    if basic_algorithms.modular_pow(g,p-1,p) == 1:
        break

print("p: " + str(p))
print("g: " + str(g))
A = basic_algorithms.modular_pow(g,a,p)
print("A: " + str(A))

b = random.randint(10 ** (len_keys - 1),10 ** len_keys)
print("b: " + str(b))
B = basic_algorithms.modular_pow(g,b,p)
print("B: " + str(B))
K_first = basic_algorithms.modular_pow(A,b,p)
K_second = basic_algorithms.modular_pow(B,a,p)
if K_first == K_second: print("Write! K = ", str(K_second))
else:
    print("Wrong")
    print(K_first)
    print(K_second)
'''
